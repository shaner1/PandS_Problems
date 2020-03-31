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

plt.plot(x, f(x), 'r', label = ("f(x) = x"))
plt.plot(x, g(x), 'g', label = ("g(x) = x^2"))
plt.plot(x, h(x), 'b', label = ("h(x) = x^3"))
plt.title("Week 8 Task")
plt.legend(loc='upper left')
plt.grid()
plt.show()

print("Program End")



