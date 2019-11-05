import numpy as np
from matplotlib import pyplot as plt

s = 500

dist = np.random.normal(0, 1, 100000)
s_sets = np.split(dist, s)

k = len(s_sets)

means = []
for i in range(s):
    means.append(np.mean(s_sets[i]))

fig0 = plt.figure()
q1 = fig0.add_subplot(111,title = 'Mean of all sets')
q1.scatter([i for i in range(s)],means)



vars = []

for k_ in range(100, k*10, 100):
    dist = np.random.normal(0, 1, s*k_)
    s_sets = np.split(dist, s)

    mean = []
    for i in range(s):
        mean.append(np.mean(s_sets[i]))
    vars.append(np.var(mean))

fig1 = plt.figure()
q1 = fig1.add_subplot(121,title='K vs variance | s = 500',xlabel='K',ylabel='variance')
q1.scatter([i for i in range(0,len(vars))],vars)




vars = []

for s_ in range(100, s*10, 100):
    dist = np.random.normal(0, 1, s*k_)
    s_sets = np.split(dist, s)

    mean = []
    for i in range(s):
        mean.append(np.mean(s_sets[i]))
    vars.append(np.var(mean))

q2 = fig1.add_subplot(122,title='s vs variance | K = 500',xlabel='s',ylabel='variance')
q2.scatter([i for i in range(0,len(vars))],vars)




plt.show()
