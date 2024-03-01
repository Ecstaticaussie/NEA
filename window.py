import tkinter as tk
from tkinter import ttk
import matplotlib.pyplot as plt
import matplotlib as mpl
import networkx as nx
"""
The libraries above are explained in my analysis
"""
from graph_code.graph_generator import graph_mapper

#Allows the graph to be updated
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
        self.iconbitmap()

    def create_buttons(self):
        #Creating buttons
        self.beginning_algorithm = ttk.Button(self, text="<<")
        self.previous_step = ttk.Button(self, text="<")
        self.generate_graph_Button = ttk.Button(self, text="Generate", command=self.create_pop_up)
        self.next_step = ttk.Button(self, text=">")
        self.end_algorithm = ttk.Button(self, text=">>")

        #Placing buttons
        self.beginning_algorithm.grid(row=0, column=0)
        self.previous_step.grid(row=0, column=1)
        self.generate_graph_Button.grid(row=0, column=2)
        self.next_step.grid(row=0, column=3)
        self.end_algorithm.grid(row=0, column=4)
    
    #Creating the pop up and placing it when it's called
    def create_pop_up(self):
        self.pop_up_frame = ttk.Frame(self)
        self.ask_label = ttk.Label(self.pop_up_frame, text="Would you like to generate a new graph?")
        self.yes_button = ttk.Button(self.pop_up_frame, text="Yes", command=self.create_random_graph)
        self.no_button = ttk.Button(self.pop_up_frame, text="No", command=self.destroy_pop_up)

        self.pop_up_frame.grid(row=1, column=0)
        self.ask_label.grid(row=0, column=0)
        self.yes_button.grid(row=1, column=0)
        self.no_button.grid(row=1, column=1)

        #Disabling the other buttons 
        self.beginning_algorithm.state = tk.DISABLED
        self.previous_step.state = tk.DISABLED
        self.generate_graph_Button.state = tk.DISABLED
        self.next_step.state = tk.DISABLED
        self.end_algorithm.state = tk.DISABLED

    #Destroys the pop up in the main window
    #This is done instead of just removing the pop up from the main window as I don't need another method
    #to just add the pop up back to the main window
    def destroy_pop_up(self):
        self.ask_label.destroy()
        self.yes_button.destroy()
        self.no_button.destroy()
        self.pop_up_frame.destroy()
  
        #Enabling the other buttons
        self.beginning_algorithm.state = tk.NORMAL
        self.previous_step.state = tk.NORMAL
        self.generate_graph_Button.state = tk.NORMAL
        self.next_step.state = tk.NORMAL
        self.end_algorithm.state = tk.NORMAL

    #Draws a graph in a seperate window
    def create_random_graph(self, remove_pop_up=True):
        if remove_pop_up: self.destroy_pop_up()
        plt.clf()
        myGraph = graph_mapper()
        pos = nx.spring_layout(myGraph)
        nx.draw(myGraph, pos, with_labels=True)