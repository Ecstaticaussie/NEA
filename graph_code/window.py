import tkinter as tk
from tkinter import ttk
import matplotlib.pyplot as plt
import matplotlib as mpl
import networkx as nx

from graph_adjuster import graph_adjuster
from dijkstra import DijkstraAlgo

#Allows the graph to be updated without closing and opening any windows
mpl.use("TkAgg")
plt.ion()

#Where the codes comes together
class Window(tk.Tk):
    def __init__(self, title, size):
        super().__init__()
        self.title(title)
        self.geometry(f"{size[0]}x{size[1]}")
        self.step_counter = 0
        self.create_random_graph()
        self.create_buttons()
        self.mainloop()

    def create_buttons(self):
        #Creating buttons
        self.num_of_nodes = self.myGraph.number_of_nodes()
        self.beginning_algorithm = ttk.Button(self, text="<<", command=lambda:self.new_step_counter(0))
        self.previous_step = ttk.Button(self, text="<", command=lambda:self.new_step_counter(self.step_counter-1))
        self.generate_graph_Button = ttk.Button(self, text="Generate", command=self.destroy_buttons)
        self.next_step = ttk.Button(self, text=">", command=lambda:self.new_step_counter(self.step_counter+1))
        self.end_algorithm = ttk.Button(self, text=">>", command=lambda:self.new_step_counter(self.num_of_nodes))

        #Placing buttons
        self.beginning_algorithm.grid(row=0, column=0)
        self.previous_step.grid(row=0, column=1)
        self.generate_graph_Button.grid(row=0, column=2)
        self.next_step.grid(row=0, column=3)
        self.end_algorithm.grid(row=0, column=4)

    #Used in self.disable_buttons()
    def enable_all_buttons(self):
        self.beginning_algorithm["state"] = "active"
        self.previous_step["state"] = "active"
        self.next_step["state"] = "active"
        self.end_algorithm["state"] = "active"

    #We first enable all buttons
    #We can then easily disable the buttons that the user shouldn't use
    #This is because we would otherwise have to check using selection when to enable the disabled buttons again.
    def disable_buttons(self):
        self.enable_all_buttons()
        if self.step_counter == 0:
            self.beginning_algorithm["state"] = "disable"
            self.previous_step["state"] = "disable"

        elif self.step_counter == self.num_of_nodes:
            self.next_step["state"] = "disable"
            self.end_algorithm["state"] = "disbale"

    #Replaces the buttons with the pop up
    def destroy_buttons(self):
        self.beginning_algorithm.destroy()
        self.previous_step.destroy()
        self.generate_graph_Button.destroy()
        self.next_step.destroy()
        self.end_algorithm.destroy()
        self.create_pop_up()

    #Creating the pop up and placing it
    def create_pop_up(self):
        self.ask_label = ttk.Label(self, text="Would you like to generate a new graph?")
        self.yes_button = ttk.Button(self, text="Yes", command=lambda: self.destroy_pop_up(create_graph=True))
        self.no_button = ttk.Button(self, text="No", command=self.destroy_pop_up)
        self.ask_label.grid(row=0, column=0, padx=100, columnspan=2)
        self.yes_button.grid(row=1, column=0)
        self.no_button.grid(row=1, column=1)

    """
    Destroys the pop up in the main window and replaces it with the other buttons

    This is done instead of just removing the pop up from the main window
    as I don't need another method to just add the pop up back to the main window
    """
    def destroy_pop_up(self, create_graph=False):
        self.ask_label.destroy()
        self.yes_button.destroy()
        self.no_button.destroy()
        if create_graph: self.create_random_graph()
        self.create_buttons()

    def shift_node_vertex_boxes(self, pos):
        pos_label = {}
        for x in pos:
            pos_label[x] = [pos[x][0]+0.01, pos[x][1]+0.01]
        return pos_label

    def next_vertex_boxes(self):
        return self.myDijkstra.dijk_step(self.step_counter)

    def new_step_counter(self, num):
        self.step_counter = num
        self.disable_buttons()
        self.display_graph()

    #Creates a random graph and execute + stores the steps of Dijkstra's
    def create_random_graph(self):
        self.myGraph, self.node_positions, self.edge_weights = graph_adjuster()
        self.node_attributes_pos = self.shift_node_vertex_boxes(self.node_positions)
        self.myDijkstra = DijkstraAlgo(self.myGraph)
        self.myDijkstra.execute()

        self.step_counter = 0
        self.display_graph(remove_pop_up=False)

    #Draws a graph in a seperate window
    def display_graph(self,remove_pop_up=False):
        if remove_pop_up: self.destroy_pop_up()
        plt.clf()

        current_vertex_boxes = self.next_vertex_boxes()
        nx.draw(self.myGraph, pos=self.node_positions, node_color="black", node_size=30, alpha=0.9)
        nx.draw_networkx_edge_labels(self.myGraph, pos=self.node_positions, edge_labels=self.edge_weights, alpha=0.7)
        nx.draw_networkx_labels(self.myGraph, pos=self.node_attributes_pos, labels=current_vertex_boxes, font_size=12, horizontalalignment="left", verticalalignment="bottom", font_weight=100)