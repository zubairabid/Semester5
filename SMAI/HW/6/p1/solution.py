import numpy as np
from sklearn.model_selection import KFold

import math
import pprint

def function(n):
    mew = 0
    sigma = 1

    # Creating the data
    noise = np.random.normal(mew, sigma, n)
    y = np.array([math.sin(i) for i in range(n)]) + noise 
    x = np.arange(n)
    data_points = np.vstack((x, y)).T

    pprint.pprint(noise)

    meanvar = []
    # Iterating through possible values of k
    for k in range(2, n):
        if n % k != 0:
            continue

        # Split, 
        fold_means = []
        kfold = KFold(k, True, 1)
        for train, test in kfold.split(noise):
            fold_means.append(np.mean(noise[train]))

        mean = np.mean(fold_means)
        var = np.var(fold_means)
        meanvar.append((k, mean, var))

    pprint.pprint(meanvar)

function(100)
