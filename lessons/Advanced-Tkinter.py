# 1. Animation: Use after() for Periodic Updates
# import tkinter as tk

# def animate():
#     current_color = label.cget("bg")
#     new_color = "red" if current_color == "green" else "green"
#     label.config(bg=new_color)
    
#     root.after(1000, animate)

# root = tk.Tk()
# root.geometry("300x200")

# label = tk.Label(root, text="Animating Color", bg="green", font=("Arial", 20))
# label.pack(pady=50)

# animate()

# root.mainloop()

# 2. Custom Widgets: Create Classes that Extend tk.Frame
# import tkinter as tk

# class CounterWidget(tk.Frame):
#     def __init__(self, master, **kwargs):
#         super().__init__(master, **kwargs)
        
#         self.counter = 0
#         self.label = tk.Label(self, text=str(self.counter), font=("Arial", 20))
#         self.label.pack(pady=20)
        
#         self.button = tk.Button(self, text="Increment", command=self.increment)
#         self.button.pack(pady=10)
        
#     def increment(self):
#         self.counter += 1
#         self.label.config(text=str(self.counter))

# root = tk.Tk()
# root.geometry("300x200")

# counter_widget = CounterWidget(root)
# counter_widget.pack(pady=20)

# root.mainloop()

# 3. Integration: Embed Charts using Matplotlib or Web Content with tkhtml
# Example (Embedding a Matplotlib Chart):
# import tkinter as tk
# from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
# import matplotlib.pyplot as plt

# root = tk.Tk()
# root.geometry("1000x700")

# fig, ax = plt.subplots(figsize=(10, 10))
# ax.plot([1, 2, 3, 4], [1, 4, 9, 16])

# canvas = FigureCanvasTkAgg(fig, master=root)
# canvas.draw()
# canvas.get_tk_widget().pack(pady=20)

# root.mainloop()

# Example (Embedding Web Content with tkhtmlview):
import tkinter as tk
from tkhtmlview import HTMLLabel

root = tk.Tk()
root.geometry("400x300")

html_content = "<h1>Hello, Tkinter!</h1><p>This is a paragraph in HTML.</p>"
html_label = HTMLLabel(root, html=html_content)
html_label.pack(pady=20)

root.mainloop()