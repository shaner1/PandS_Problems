#This program displays a plot of the functions f(x)=x, g(x)=x2 and h(x)=x3 in the range [0, 4] on the one set of axes.

import numpy as np 
import matplotlib.pyplot as plt

# define the function y = x 
def f(x):
    return x 

# define the function y = x^2
def g(x): 
    return x **2

# define the function y = x^3
def h(x): 
    return x **3

# set the range of x 0 - 4 and go up in steps of 0.01 
x = np.linspace(0.0, 5.0, 100)

#plots the x & y coordinates for each function, assigns them a colour and a label
plt.plot(x, f(x), 'r', label = ("f(x) = x"))
plt.plot(x, g(x), 'g', label = ("g(x) = x^2"))
plt.plot(x, h(x), 'b', label = ("h(x) = x^3"))
# Gives the plot a title
plt.title("Week 8 Task")
# creates a legend based on the predefined labels and locates it in the upper left corner
plt.legend(loc='upper left')
# displays the plot on a grid 
plt.grid()
plt.show()





