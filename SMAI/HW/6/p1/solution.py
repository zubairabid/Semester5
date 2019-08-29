import numpy as np
from sklearn.model_selection import KFold
from matplotlib import pyplot as plt

import math
import pprint

index = 1
fig = plt.figure()

def plot(k, mean, var, n):

    global fig
    global index

    ax = fig.add_subplot(2, 2, index, title="Mean vs K for n = {0}".format(n))
    plt.plot(k, mean)

    ax = fig.add_subplot(2, 2, index+1, title="Variance vs K for n = {0}".format(n))
    plt.plot(k, var)

    index += 2

def function(n):
    mew = 0
    sigma = 1

    # Creating the data
    noise = np.random.normal(mew, sigma, n)
    y = np.array([math.sin(i) for i in range(n)]) + noise 
    x = np.arange(n)
    data_points = np.vstack((x, y)).T

    # pprint.pprint(noise)

    ks = []
    means = []
    variances = []
    # Iterating through possible values of k
    for k in range(2, n):
        if n % k != 0:
            continue

        # Split, 
        fold_means = []
        kfold = KFold(k, True, 1)
        for train, test in kfold.split(noise):
            fold_means.append(np.mean(noise[train]))

        means.append(np.mean(fold_means))
        variances.append(np.var(fold_means))
        ks.append(k)

    plot(ks, means, variances, n)

function(100)
function(10000)
plt.show()

