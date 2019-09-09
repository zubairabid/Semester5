import numpy as np

w1 = [[0, 0], [0, 1], [2, 0], [3, 2], [3, 3], [2, 2], [2, 0]]

w2 = [
    [7, 7],
    [8, 6],
    [9, 7],
    [8, 10],
    [7, 10],
    [8, 9],
    [7, 11],
    ]


print(np.mean(w1, axis=0))
print(np.mean(w2, axis=0))
print(np.cov(np.transpose(w1)))
print(np.cov(np.transpose(w2)))
