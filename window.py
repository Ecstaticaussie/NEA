import tkinter as tk
from tkinter import ttk
import matplotlib.pyplot as plt
import matplotlib as mpl
import networkx as nx
from graph_code.graph_generator import graph_mapper
mpl.use("TkAgg")
plt.ion()

class Window(tk.Tk):
    def __init__(self, title, size):
        super().__init__()
        self.title(title)
        self.geometry(f"{size[0]}x{size[1]}")
        self.create_buttons()
        self.mainloop()

    def create_buttons(self):
        self.beginning_algorithm = ttk.Button(self, text="<<")
        self.previous_step = ttk.Button(self, text="<")
        self.generate_graph_Button = ttk.Button(self, text="Generate", command=self.create_random_graph)
        self.next_step = ttk.Button(self, text=">")
        self.end_algorithm = ttk.Button(self, text=">>")

        self.beginning_algorithm.grid(row=0, column=0)
        self.previous_step.grid(row=0, column=1)
        self.generate_graph_Button.grid(row=0, column=2)
        self.next_step.grid(row=0, column=3)
        self.end_algorithm.grid(row=0, column=4)

    def create_random_graph(self):
        plt.clf()
        myGraph = graph_mapper()
        pos = nx.spring_layout(myGraph)
        nx.draw(myGraph, pos, with_labels=True)