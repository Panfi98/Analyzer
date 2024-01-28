import matplotlib.pyplot as plt
import numpy as np

class Plotter:
    """ This class structures plotting. It takes in x-values and y-values as the fir"""
    def __init__(self,x,y, x_name, y_name, title,legend):
        self.x = x
        self.y = y
        self.x_name = x_name
        self.y_name = y_name
        self.legend = legend
        self.title = title

    def plot_data(self):
        plt.plot(self.x, self.y)
        plt.legend([f"{self.legend}"])
        plt.title(f"{self.title}")
        plt.xlabel(f"{self.x_name}]")
        plt.ylabel(f"{self.y_name}")
        plt.show()


