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
        generate_graph_Button = ttk.Button(self, text="Generate")
        next_step = ttk.Button(self, text=">")
        end_algorithm = ttk.Button(self, text=">>")

        beginning_algorithm.grid(row=1, column=0)
        previous_step.grid(row=1, column=1)
        generate_graph_Button.grid(row=1, column=2)
        next_step.grid(row=1, column=3)
        end_algorithm.grid(row=1, column=4)