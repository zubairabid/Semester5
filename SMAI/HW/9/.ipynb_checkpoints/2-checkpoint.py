import numpy as np
from matplotlib import pyplot as plt

fig1 = plt.figure()

def gradient_descent(x,n=0.1,iterations=5,limit=0):
    xs = [-2]
    ys = [4]
    for i in range(iterations):
        x -= n * 2 * x  # dy/dx of x^2 is 2x
        xs.append(x)
        ys.append(x*x)
        if x*x < limit:
            return i    
    return xs,ys


if __name__ == "__main__":
    x1s,y1s = gradient_descent(x=-2,iterations=1000)

    p1 = fig1.add_subplot(121,title='First 5 errors',xlabel='iterations',ylabel='errors')
    p1.plot(y1s[:5])
    
    p2 = fig1.add_subplot(122,title='First 1000 iterations',xlabel='iterations',ylabel='errors')
    p2.plot(y1s)
    
    fig2 = plt.figure()
    x3s,y3s = gradient_descent(x=-2,n=0.4,iterations=1000)
    p3 = fig2.add_subplot(131,title='n=0.4',xlabel='iterations',ylabel='errors')
    p3.plot(x3s)

    x4s,y4s = gradient_descent(x=-2,n=1,iterations=1000)
    p4 = fig2.add_subplot(132,title='n=1',xlabel='iterations',ylabel='errors')
    p4.scatter([i for i in range(len(x4s))],x4s,s=0.2)

    x5s,y5s = gradient_descent(x=-2,n=1.2,iterations=1000)
    p5 = fig2.add_subplot(133,title='n=2',xlabel='iterations',ylabel='errors')
    p5.scatter([i for i in range(len(x5s))],x5s,s=0.3)
    
    fig3 = plt.figure()
    iterations = []
    for i in range(10,100000,100):
        iterations.append(gradient_descent(x=-2,n=0.4,iterations=100000,limit=1/i))
    p6 = fig3.add_subplot(111,title='',xlabel='1/convergance criteria',ylabel='iterations')
    p6.plot(iterations)
    plt.show()