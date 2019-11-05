import numpy as np
from matplotlib import pyplot as plt

fig2 = plt.figure()
p21 = fig2.add_subplot(111,title = 'Mean of all s sets',xlabel='set',ylabel='mean')

data = np.random.normal(0,1,10000)
sets = np.split(data,200)
means = []
for i in range(200):
    means.append(np.mean(sets[i]))
p21.scatter([i for i in range(200)],means)

vars = []

for x in range(200,100000,200):
    data = np.random.normal(0,1,x)
    sets = np.split(data,200)
    mle = []
    for i in range(200):
        mle.append(np.mean(sets[i]))
    vars.append(np.var(mle))

fig = plt.figure()
p1 = fig.add_subplot(121,title='K vs variance | s = 200',xlabel='k',ylabel='variance')
p1.scatter([i for i in range(0,len(vars))],vars)

vars = []
for x in range(1,201):
    # k = 500
    data = np.random.normal(0,1,500*x)
    sets = np.split(data,x)
    mle = []
    for i in range(x):
        mle.append(np.mean(sets[i]))
    vars.append(np.var(mle))

p2 = fig.add_subplot(122,title='s vs variance | k = 500',xlabel='s',ylabel='variance')
p2.scatter([i for i in range(0,len(vars))],vars)

plt.show()
