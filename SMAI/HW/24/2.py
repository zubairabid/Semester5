import numpy as np
import matplotlib.pyplot as plt

def gline(x):
        v_, c_ = np.linalg.eig(np.cov(x.T))
        idx = np.argsort(v_)[::-1]
        v = c_[:,idx][:,0]
        m = v[1]/v[0]
        c = np.mean(x[:,1]) - m*np.mean(x[:,0])
        return m, c

def dist(X, m, c):
        x, y = X

        d1 = np.abs(y-m[0]*x-c[0])/np.sqrt(1+m[0]*m[0])
        d2 = np.abs(y-m[1]*x-c[1])/np.sqrt(1+m[1]*m[1])
        
        if d1 >= d2:
                return 1
        else:
                return 2

# Data Generation
data = []
for i in range(-100,100):
        data.append([i,i+np.random.normal(0,10)])
        data.append([i,-i + np.random.normal(0,10)])
data = np.array(data)

plt.subplot(1,2,1)
plt.scatter(data[:,0],data[:,1])
plt.title("Original Data")

labels = np.ones(400)
labels[np.random.choice(400,200,replace=False)] = 2
i = 0
while True:

        chk_labels = np.copy(labels)
        m1, c1 = gline(data[labels==1])
        m2, c2 = gline(data[labels==2])
        for idx, j in enumerate(data):
                labels[idx] = dist(j, [m1, m2], [c1, c2])

        i += 1

        if np.all(chk_labels == labels) or i == 100:
                break

plt.subplot(1,2,2)
plt.scatter(data[:,0][labels==1],data[:,1][labels==1],label="First Class")
plt.scatter(data[:,0][labels==2],data[:,1][labels==2],label="Second Class")
plt.title("Clustered data")
plt.legend()
plt.show()
