import numpy as np
import matplotlib.pyplot as plt

init_x = -2
learn_rate = 0.1

def grad_desc(init_x, learn_rate, iterations=500, lim=0):
    x_a = [init_x]
    y_a = [init_x**2]

    x = init_x

    for i in range(iterations):
        x -= learn_rate*2*x;
        
        x_a.append(x)
        y_a.append(x**2)

        if x**2 < lim:
            return i

    return x_a, y_a


fig = plt.figure()

x1, y1 = grad_desc(init_x, learn_rate)
print("Minima at x = {0}".format(x1[-1]))

q1 = fig.add_subplot(121, title="First 5", xlabel="Iteration count", ylabel="Error")
q1.plot(y1[:5])

q1 = fig.add_subplot(122, title="30 iterations, observing minima", xlabel="Iteration count", ylabel="Error")
q1.plot(y1[:30])


xconv, yconv = grad_desc(init_x, 0.5)
xdiv, ydiv = grad_desc(init_x, 1)
xosc, yosc = grad_desc(init_x, 3)

fig2 = plt.figure()

q1 = fig2.add_subplot(131, title="n = 0.5: Converge", xlabel="Iteration count", ylabel="Error")
q1.plot(xconv[:100])
q2 = fig2.add_subplot(132, title="n = 1: Oscillating", xlabel="Iteration count", ylabel="Error")
q2.scatter([num for num in range(len(xdiv[:100]))], xdiv[:100], s=0.1)
q3 = fig2.add_subplot(133, title="n = 1.5: Diverging", xlabel="Iteration count", ylabel="Error")
q3.plot(xosc[:100])


plt.show()
