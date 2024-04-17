import tkinter as tk
from tkinter import ttk
import matplotlib.pyplot as plt
import matplotlib as mpl
import networkx as nx
"""
The libraries above are explained in my analysis
"""
from graph_code.graph_adjuster import graph_adjuster

#Allows the graph to be updated without closing and opening any windows
mpl.use("TkAgg")
plt.ion()

#Where the codes comes together
class Window(tk.Tk):
    def __init__(self, title, size):
        super().__init__()
        self.title(title)
        self.geometry(f"{size[0]}x{size[1]}")
        self.create_buttons()
        self.create_random_graph(remove_pop_up=False)
        self.mainloop()

    def create_buttons(self):
        #Creating buttons
        self.beginning_algorithm = ttk.Button(self, text="<<")
        self.previous_step = ttk.Button(self, text="<")
        self.generate_graph_Button = ttk.Button(self, text="Generate", command=self.destroy_buttons)
        self.next_step = ttk.Button(self, text=">")
        self.end_algorithm = ttk.Button(self, text=">>")

        #Placing buttons
        self.beginning_algorithm.grid(row=0, column=0)
        self.previous_step.grid(row=0, column=1)
        self.generate_graph_Button.grid(row=0, column=2)
        self.next_step.grid(row=0, column=3)
        self.end_algorithm.grid(row=0, column=4)

    #Replaces the buttons with the pop up
    def destroy_buttons(self):
        self.beginning_algorithm.destroy()
        self.previous_step.destroy()
        self.generate_graph_Button.destroy()
        self.next_step.destroy()
        self.end_algorithm.destroy()
        self.create_pop_up()

    #Creating the pop up and placing it when it's called
    def create_pop_up(self):
        self.ask_label = ttk.Label(self, text="Would you like to generate a new graph?")
        self.yes_button = ttk.Button(self, text="Yes", command=self.create_random_graph)
        self.no_button = ttk.Button(self, text="No", command=self.destroy_pop_up)
        self.ask_label.grid(row=0, column=0, padx=100, columnspan=2)
        self.yes_button.grid(row=1, column=0)
        self.no_button.grid(row=1, column=1)

    #Destroys the pop up in the main window and replaces it with the other buttons
    #This is done instead of just removing the pop up from the main window as I don't need another method
    #to just add the pop up back to the main window
    def destroy_pop_up(self):
        self.ask_label.destroy()
        self.yes_button.destroy()
        self.no_button.destroy()
        self.create_buttons()

    #Draws a graph in a seperate window
    def create_random_graph(self, remove_pop_up=True):
        if remove_pop_up: self.destroy_pop_up()
        plt.clf()
        myGraph, node_positions, edge_weights = graph_adjuster()
        nx.draw(myGraph, with_labels=True, pos=node_positions, node_color="red")
        nx.draw_networkx_edge_labels(myGraph, pos=node_positions, edge_labels=edge_weights, alpha=0.7)