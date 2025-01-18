# 1. Introduction
"""
Tkinter is Python's de-facto GUI package that comes pre-installed.
It is built on the Tk GUI toolkit and provides a simple interface for building desktop applications.
"""

# 2. Setting Up Tkinter
import tkinter as tk
from tkinter import ttk  # For themed widgets

"""
tk: Core library.
ttk: Provides modern-looking widgets
"""

# 3. Main Window
root = tk.Tk()
root.title("My Application")
root.geometry("500x500")  # Set width x height

# 4. Widgets Overview

# Button
button = tk.Button(root, text="Click Me", command=lambda: print("Button clicked"))
button.pack()


# Label
label = tk.Label(root, text="This is a Label")
label.pack()

# Entry (Input Box)
entry = tk.Entry(root)
entry.pack()

# Text (Multiline Text)
text = tk.Text(root, height=5, width=30)
text.pack()

# Checkbutton
var = tk.IntVar()
checkbox = tk.Checkbutton(root, text="Check me!", variable=var)
checkbox.pack()

# Radiobutton
choice = tk.StringVar()
radio1 = tk.Radiobutton(root, text="Option 1", value="1", variable=choice)
radio2 = tk.Radiobutton(root, text="Option 1", value="2", variable=choice)
radio1.pack()
radio2.pack()

# Combobox (Dropdown)
combo = ttk.Combobox(root, values=["Option 1", "Option 2", "Option 3"])
combo.pack()

# Layouts
# pack()
button2 = tk.Button(root, text="Left")
button2.pack(side="left", padx=10, pady=10)

button3 = tk.Button(root, text="Right")
button3.pack(side="right", padx=10, pady=10)

# grid()

# place()
button4 = tk.Button(root, text="Placed")
button4.place(x=100, y=100)


# 6. Event Handling

def on_click(e):
    print("You clicked at", e.x, e.y)

root.bind("<Button-1>", on_click) 

# 7. Themed Widgets with ttk
button4 = ttk.Button(root, text="Themed Button")
button4.pack()


# 8. Canvas for Drawing
canvas = tk.Canvas(root, width=200, height=200)
canvas.pack()
canvas.create_rectangle(50, 50, 150, 150, fill="blue")

# 9. Menu Bars
menu = tk.Menu(root)
root.config(menu=menu)
file_menu = tk.Menu(menu, tearoff=0)
file_menu.add_command(label="Open")
file_menu.add_command(label="Save")
file_menu.add_command(label="Exit", command=root.quit)
menu.add_cascade(label="File", menu=file_menu)

# 10. Dialogs

# Message Box
# from tkinter import messagebox, filedialog
# messagebox.showinfo("Title", "Message Content")


# File Dialog
# file_path = filedialog.askopenfilename()


# 11. Frames
# frame = tk.Frame(root, bg="blue")
# frame.pack(fill="both", expand=True)

# 12. Customizing Widgets
custom_button = tk.Button(root, text="custom button")
custom_button.pack()
custom_button.config(bg="blue", fg="white", font=("Arial", 12))


# 13. Multithreading. For handling background tasks
import threading
def background_task():
    print("Task running")

thread = threading.Thread(target=background_task)
thread.start()