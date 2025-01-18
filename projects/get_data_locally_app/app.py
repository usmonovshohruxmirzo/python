import tkinter as tk
from tkinter import ttk
import psycopg2
import requests
import threading

SUPABASE_URL = "https://hqohzlpcxyqpgfnqgqdw.supabase.co"
SUPABASE_ANON_KEY = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6Imhxb2h6bHBjeHlxcGdmbnFncWR3Iiwicm9sZSI6InNlcnZpY2Vfcm9sZSIsImlhdCI6MTczNTAxNjQxMiwiZXhwIjoyMDUwNTkyNDEyfQ.XZ_nIVunvPOtO-qTJkB3y7ajKhnVYqNiMR9CtEM3KJc"
SUPABASE_BOOKS_TABLE = "books"

supabase_headers = {
    "apiKey": f"{SUPABASE_ANON_KEY}",
    "Content-Type": "application/json"
}

def fetch_books_from_psql():
    try:
        conn = psycopg2.connect(
            dbname="webbro-academy", 
            user="postgres", 
            password="usmonovdev777", 
            host="localhost", 
            port="5432"
        )
        cursor = conn.cursor()

        cursor.execute("SELECT * FROM books")
        rows = cursor.fetchall()
        columns = [desc[0] for desc in cursor.description]

        if rows:
            display_table(columns, rows)
            sync_data_from_supabase(cursor, conn)
        else:
            label_table.config(text="No books found in the database.")

        conn.close()
    except Exception as e:
        label_table.config(text=f"Error: {e}")

def display_table(columns, rows):
    for widget in frame_table.winfo_children():
        widget.destroy()

    tree = ttk.Treeview(frame_table, columns=columns, show="headings")

    for col in columns:
        tree.heading(col, text=col)
        tree.column(col, width=200)

    for row in rows:
        tree.insert("", "end", values=row)

    tree.pack(fill=tk.BOTH, expand=True)

def sync_data_from_supabase(cursor, conn):
    try:
        response = requests.get(f"{SUPABASE_URL}/rest/v1/{SUPABASE_BOOKS_TABLE}", headers=supabase_headers)
        response.raise_for_status()
        books_data = response.json()

        if books_data:
            cursor.execute("SELECT id FROM books")
            local_books = cursor.fetchall()
            local_book_ids = {book[0] for book in local_books}

            for book in books_data:
                if book['id'] not in local_book_ids:
                    cursor.execute(f"INSERT INTO books (id, title, book_thumbnail, link) VALUES (%s, %s, %s, %s)",
                                   (book['id'], book['title'], book['book_thumbnail'], book['link']))
                    local_book_ids.add(book['id'])

            for book_id in local_book_ids:
                if not any(book['id'] == book_id for book in books_data):
                    cursor.execute(f"DELETE FROM books WHERE id = %s", (book_id,))

            conn.commit()

            label_table.config(text="Local PostgreSQL database synced with Supabase.")
        else:
            label_table.config(text="No books data found in Supabase.")
    except requests.exceptions.RequestException as e:
        label_table.config(text=f"Error syncing data from Supabase: {e}")
        print(f"Error syncing data from Supabase: {e}")

def poll_for_new_data():
    while True:
        fetch_books_from_psql()
        time.sleep(1)

import time
polling_thread = threading.Thread(target=poll_for_new_data, daemon=True)
polling_thread.start()

root = tk.Tk()
root.title("App")
root.geometry("800x600")

label_table = tk.Label(root, text="", font=("Arial", 12), fg="red")
label_table.pack(pady=10)

frame_table = tk.Frame(root)
frame_table.pack(fill=tk.BOTH, expand=True)

fetch_books_from_psql()

root.mainloop()