import numpy as np
import matplotlib.pyplot as plt
from sklearn import svm, datasets


def krnl(X, Y):
	'''
	Kernel transform for SVM
	'''
    print(X.shape, Y.shape)
    return np.power(1 + X@Y.T, 3)


data = np.array([
	[1, 1],
	[-1, -1],
	[1, -1],
	[-1, 1]
])
y = np.array([1, 1, -1, -1])
h = .02
c_ = [1e-5, 0.1, 10, 1e5]


fig1 = plt.subplots(4, 1, figsize=(10,10))[1]


for ind,C in enumerate(c_):

    svc = svm.SVC(kernel=krnl, C=C).fit(data, y)
    rbf_svc = svm.SVC(kernel='rbf', gamma=0.7, C=C).fit(data, y)
    poly_svc = svm.SVC(kernel='poly', degree=2, C=C).fit(data, y)
    lin_svc = svm.LinearSVC(C=C).fit(data, y)

    data_min, data_max = data[:, 0].min()-1, data[:, 0].max()+1
    y_min, y_max = data[:, 1].min()-1, data[:, 1].max()+1
    
    xx, yy = np.meshgrid(np.arange(data_min, data_max, h),
                         np.arange(y_min, y_max, h))

    titles = ['my kernel',
              'linear kernel',
              'RBF kernel',
              'poly kernel']


    for i, clf in enumerate((svc, lin_svc, rbf_svc, poly_svc)):

        plt.subplot(4, 4,ind + i*4 + 1)
        plt.subplots_adjust(wspace=0.4, hspace=0.4)

        Z = clf.predict(np.c_[xx.ravel(), yy.ravel()])

        Z = Z.reshape(xx.shape)
        plt.contourf(xx, yy, Z, cmap=plt.cm.coolwarm, alpha=0.8)

        plt.scatter(data[:, 0], data[:, 1], c=y, cmap=plt.cm.coolwarm)
        plt.xlabel('X - axis')
        plt.ylabel('Y - axis')
        plt.xlim(xx.min(), xx.max())
        plt.ylim(yy.min(), yy.max())
        plt.xticks(())
        plt.yticks(())
        plt.title(titles[i]+'with C = '+str(C))

plt.show()



