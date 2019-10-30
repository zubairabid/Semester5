import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D


def sigmoid(x):
    return 1/(1 + np.exp(-x))


def MSE_Loss(w, data, y):
    total = len(data)
    one_row = np.ones(total)
    x = np.vstack((data, one_row))
    a = np.dot(w.T, x)
    return np.sum((y - a)**2)/ total


def MSE_Logistic_Loss(w, data, y):
    total = len(data)
    one_row = np.ones(total)
    x = np.vstack((data, one_row))
    a = sigmoid(np.dot(w.T, x))
    return np.sum((y - a)**2)/ total


N = 500
D1 = np.random.normal(1, 3, size = N)
D2 = np.random.normal(-1, 3, size = N)

data = np.concatenate((D1,D2), axis = 0)
one_row = np.ones(N)
label = np.concatenate((one_row, -one_row), axis = 0)


x = np.linspace(-25, 25, 100)
X, Y = np.meshgrid(x, x)


Z1 = []
Z2 = []

for i in range(len(X)):
    row_simple = []
    row_logistic = []
    for j in range(len(Y)):
        w = np.array([X[i][j], Y[i][j]])
        row_simple.append(MSE_Loss(w, data, label))
        row_logistic.append(MSE_Logistic_Loss(w, data, label))
    Z1.append(row_simple)
    Z2.append(row_logistic)
Z1 = np.array(Z1)
Z2 = np.array(Z2)

fig = plt.figure(figsize = (10, 10))
ax1 = fig.add_subplot(121, projection = "3d")
ax2 = fig.add_subplot(122, projection = "3d")

ax1.plot_wireframe(X, Y, Z1)
ax1.set_title("Simple MSE Loss (Convex)")
ax2.plot_wireframe(X, Y, Z2)
ax2.set_title("Logistic MSE Loss (Non-Convex)")
plt.show()
