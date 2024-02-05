import tkinter as tk
from tkinter import ttk
import matplotlib.pyplot as plt
import networkx as nx
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from graph_code.graph_generator import graph_generator

class Window(tk.Tk):
    def __init__(self, title, size):
        super().__init__()
        self.title(title)
        self.geometry(f"{size[0]}x{size[1]}")
        self.create_buttons()
        #self.create_random_graph()
        self.mainloop()

    def create_buttons(self):
        beginning_algorithm = ttk.Button(self, text="<<")
        previous_step = ttk.Button(self, text="<")
        generate_graph_Button = ttk.Button(self, text="Generate", command=self.create_random_graph)
        next_step = ttk.Button(self, text=">")
        end_algorithm = ttk.Button(self, text=">>")

        #Use of .grid() will change
        beginning_algorithm.grid(row=1, column=0)
        previous_step.grid(row=1, column=1)
        generate_graph_Button.grid(row=1, column=2)
        next_step.grid(row=1, column=3)
        end_algorithm.grid(row=1, column=4)

    """#Used to show no graph when the user opens up the program
    def create_blank_graph(self):
        blank_graph = nx.Graph()
        blank_axis = nx.draw(blank_graph, with_labels=True, font_weight='bold')
        canvas = FigureCanvasTkAgg(blank_axis, master=self)
        canvas.get_tk_widget().grid(row=0, column=2)"""

    def create_random_graph(self):
        myGraph = graph_generator()
        graph_axis = nx.draw_networkx(myGraph, with_labels=True, font_weight='bold')
        subaxis = plt.subplot(121)
        canvas = FigureCanvasTkAgg(graph_axis, master=self)
        canvas.get_tk_widget().grid(row=0, column=2)