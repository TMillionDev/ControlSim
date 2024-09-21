import numpy as np
from matplotlib import pyplot as plt

def PID(P, I, D):
   plt.rcParams["figure.figsize"] = [7.50, 3.50]
   plt.rcParams["figure.autolayout"] = True

   def f(p, i, d):
      return p * x * x + i * x + d

   x = np.linspace(10, 100)

   plt.plot(x, f(P, I, D), color='red')

   plt.show()