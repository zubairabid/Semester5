import numpy as np
from pprint import pprint
import matplotlib.pyplot as plt
import numpy as np
import random

def plot(val, vec):
    plt.plot(linex, liney, color="red")
    plt.scatter(pointsx, pointsy, s=1)
    plt.quiver(origin, vec[:,0], vec[:,1], scale=5)
    plt.show()

def calculate():
    covariance = np.cov(pointsx, pointsy)

    egval, egvec = np.linalg.eig(covariance)
    return egval, egvec 


# Line generation
linex = np.linspace(-10, 10, 100)
liney = -linex - 1

# Point generation
pointsx = np.linspace(-9, 9, 1000)
pointsy = []

for xval in pointsx:
    yval = -xval - 1
    yval += random.randrange(-2, 3)

    pointsy.append(yval)

origin = [np.mean(pointsx), np.mean(pointsy)]


# Work
val, vec = calculate()
plot(val, vec)

