import numpy as np
import matplotlib.pyplot as plt

# This import registers the 3D projection, but is otherwise unused.
from mpl_toolkits.mplot3d import Axes3D  # noqa: F401 unused import

from pprint import pprint


def plot(mew1, mew2, sig1, sig2):
    a = np.random.multivariate_normal(mew1, sig1, size=1000)
    b = np.random.multivariate_normal(mew2, sig1, size=1000)

    fig = plt.figure()

    ax = fig.add_subplot(2, 2, 1, projection='3d', title='3D')
    plt.scatter(a[:,0], a[:,1], a[:,2], marker='x')
    plt.scatter(b[:,0], b[:,1], b[:,2], marker='o')

    ax = fig.add_subplot(2, 2, 2, title='XY')
    plt.scatter(a[:,0], a[:,1], marker='x')
    plt.scatter(b[:,0], b[:,1], marker='o')

    ax = fig.add_subplot(2, 2, 3, title='YZ')
    plt.scatter(a[:,1], a[:,2], marker='x')
    plt.scatter(b[:,1], b[:,2], marker='o')

    ax = fig.add_subplot(2, 2, 4, title='XZ')
    plt.scatter(a[:,0], a[:,2], marker='x')
    plt.scatter(b[:,0], b[:,2], marker='o')


    plt.show()


mew1 = [1, 3, 5]
mew2 = [7, 9, 11]
sig1 = [
        [7, 0, 0],
        [0, 7, 0],
        [0, 0, 7]
        ]
sig2 = [
        [4, -3, 0],
        [-3, 4, -3],
        [0, -3, 4]
        ]

plot(mew1, mew2, sig1, sig1)
plot(mew1, mew2, sig2, sig2)
plot(mew2, mew2, sig1, sig1)

