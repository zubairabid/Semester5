import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

data = pd.read_csv("wine.data", header=None)

labels = data[data.columns[:1]]
data = data[data.columns[1:]]

mean = data.mean(axis=0)
ndata = (data-data.mean())/(data.std())

cov = ndata.cov()
w, v = np.linalg.eigh(cov)

fig = plt.figure()
q1 = fig.add_subplot(111, title="Plotting normalised covariance")
q1.scatter(range(len(w)), w)

l2 = v[:,-2:]
fin = ndata.dot(l2)
fin = np.matrix(fin)

fig2 = plt.figure()
q1 = fig2.add_subplot(111, title="Projected Data")
q1.scatter(np.array(fin[:59,0]),np.array(fin[:59,1]),c='r')
q1.scatter(np.array(fin[59:131,0]),np.array(fin[59:131,1]),c='y')
q1.scatter(np.array(fin[131:,0]),np.array(fin[131:,1]),c='b')

plt.show()
