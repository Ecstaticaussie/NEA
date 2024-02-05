import tkinter as tk
from tkinter import ttk

class Window(tk.Tk):
    def __init__(self, title, size):
        super().__init__()
        self.title(title)
        self.geometry(f"{size[0]}x{size[1]}")
        self.create_buttons()
        self.mainloop()

    def create_buttons(self):
        beginning_algorithm = ttk.Button(self, text="<<")
        previous_step = ttk.Button(self, text="<")
        next_step = ttk.Button(self, text=">")
        end_algorithm = ttk.Button(self, text=">>")

        beginning_algorithm.grid(row=1, column=0)
        previous_step.grid(row=1, column=1)
        next_step.grid(row=1, column=2)
        end_algorithm.grid(row=1, column=3)

window1 = Window(("Decoding Dijkstra's"), (1100, 600))