import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn import svm, metrics
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA


from __future__ import print_function

def read_data(filename):
    with open(filename, 'r') as f:
        lines = f.readlines()
    
    num_points = len(lines)
    dim_points = 28 * 28
    data = np.empty((num_points, dim_points))
    labels = np.empty(num_points)
    
    for ind, line in enumerate(lines):
        num = line.split(',')
        labels[ind] = int(num[0])
        data[ind] = [ int(x) for x in num[1:] ]
        
    return (data, labels)

train_data, train_labels = read_data("sample_train.csv")
test_data, test_labels = read_data("sample_test.csv")
print(train_data.shape, test_data.shape)
print(train_labels.shape, test_labels.shape)




def classify_svm(train_data, train_labels, test_data, test_labels, C=1.0, kernel='linear'):
    classifier = svm.SVC(C=C, kernel=kernel)
    
    pipeline = Pipeline([
        ('scaling', StandardScaler()),
        ('svm', classifier),
    ])

    pipeline.fit(train_data, train_labels)
    print("The classification accuracy for C = {0} is {1}".format(C, pipeline.score(test_data, test_labels)))
    
    return classifier





for c in [1000, 10, 1, 0.5, 0.1]:
    classify_svm(train_data, train_labels, test_data, test_labels, C=c)




data_label1 = train_12[train_12l==1]
data_label2 = train_12[train_12l==2]

mask = np.logical_or(train_labels==1,train_labels==2)
train_12 = train_data[mask]
train_12l = train_labels[mask]

mask = np.logical_or(test_labels==1,test_labels==2)
test_12 = test_data[mask]
test_12l = test_labels[mask]




C = np.cov(train_12.transpose())    
eigvals, eigvecs = np.linalg.eigh(C)
eigvals = eigvals[::-1]
eigvecs = eigvecs.T[::-1]
pc2d = eigvecs[:2,:]

projected_train12 = np.dot(train_12, pc2d.T )
projected_test12 = np.dot(test_12, pc2d.T)

projected_data1 = np.dot(data_label1, pc2d.T ).real
projected_data2 = np.dot(data_label2, pc2d.T ).real
plt.scatter(projected_data1[:,1],projected_data1[:,0],c='b', s=1)
plt.scatter(projected_data2[:,1],projected_data2[:,0],c='r', s=1)
plt.title("PCA to 2D and classes 1 and 2")




classifier = classify_svm(projected_train, train_12l, projected_test, test_12l, C=0.1, kernel='linear')



plt.rcParams['figure.figsize'] = [10,10]
w = classifier.coef_[0]
sl = -w[0]/w[1]

xrange = np.linspace(-400, 400)
yrange = sl * xrange - classifier.intercept_[0]/w[1]

plt.scatter(projected_data1[:,0],projected_data1[:,1], c='b', s=1)
plt.scatter(projected_data2[:,0],projected_data2[:,1], c='r', s=1)
plt.plot(xrange, yrange)

support_vecs = classifier.support_vectors_
plt.scatter(support_vecs[:, 0], support_vecs[:, 1], marker='x', c='g')

plt.title("Visualising the Decision Boundary, and support vectors")
plt.show()



plt.scatter(support_vecs[:, 0], support_vecs[:, 1], marker='x', c='g')

plt.title("Visualising the support vectors")
plt.show()





