import numpy as np
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans

data = np.array([
    [85,70],
    [71,80],
    [60,78],
    [30,45],
    [55,52],
    [5,3],
    [10,15],
    [15,12],
    [24,10],
    [80,91],
])

plt.scatter(data[:,0],data[:,1], label='Real Position')
plt.show()


kmeans = KMeans(n_clusters=2)
kmeans.fit(data)

print(kmeans.cluster_centers_, kmeans.labels_)

plt.scatter(data[:,0],data[:,1], c=kmeans.labels_, cmap='rainbow')
plt.show()


plt.scatter(data[:,0], data[:,1], c=kmeans.labels_, cmap='rainbow')
plt.scatter(kmeans.cluster_centers_[:,0] ,kmeans.cluster_centers_[:,1], color='black')
plt.show()
