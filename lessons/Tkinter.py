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
# label2 = tk.Label(root, text="This is a Label")
# label2.grid(row=0, column=0)

root.mainloop()  # Start the GUI loop