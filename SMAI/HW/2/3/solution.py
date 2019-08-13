import numpy as np
import pickle
from pprint import pprint
import matplotlib.pyplot as plt



def generate():
    data = []
    print("Looking for gendata.pkl file")
    try:
        with open('gendata.pkl', 'rb') as f:
            print("Found gendata.pkl. Not generating new data.")
            data = pickle.load(f)

    except FileNotFoundError:
        print("Did not find gendata.pkl file. Generating new data")
        with open('gendata.pkl', 'wb') as f:
            for i in range(100):
                data.append(np.insert(
                   np.random.uniform(low=-1.0, high=1.0, size=2), 2, 1))
            pickle.dump(data, f)

    return data


def accuracy(classifier):
    value = 0

    for i in a:
        if np.dot(classifier, i) > 0:
            value += 1

    for i in b:
        if np.dot(classifier, i) <= 0:
            value += 1

    return value

def plotter():
    plt.scatter(a[:,0], a[:,1], marker='o')
    plt.scatter(b[:,0], b[:,1], marker='x')

    filler = np.linspace(-1, 1, 100)
    plt.plot(filler, -filler)
    plt.plot(filler, filler+5)
    plt.plot(filler, -filler-0.3)
    

    plt.show()


data = generate()
pprint(data)

a = np.array(data[0:50])
b = np.array(data[50:100])

classifiers = [
        np.array([1,1,0]),
        np.array([-1, -1, 0]),
        np.array([0,0.5,0]),
        np.array([1, -1, 5]),
        np.array([1,1,0.3]),
    ]

for classifier in classifiers:
    print("For classifier: ", classifier)
    print("Accuracy of the classifier: ", accuracy(classifier))

plotter()
