import numpy as np
import matplotlib as plt

points = [
    [1, 1, 1],
    [-1, -1, 1],
    [2, 2, 1],
    [-2, -2, 1],
    [-1, 1, 1],
    [1, -1, 1]
]
points = np.array(points)
labels = np.array([-1, -1, 1, -1, 1, 1])

def batch_perceptron(w, iteration=0):
    
    iteration += 1
    print("At iteration {0} working with w = {1}".format(iteration, w))
    if iteration > 100:
        return (0, 0, 0)
    
    errors = []
    error_label_real = []
    n = 0.3
    
    # Check for errors
    for ind, point in enumerate(points):
        if np.dot(w, point)*labels[ind] < 0:
            errors.append(point)
            error_label_real.append(labels[ind])
    # In case of no errors
    if len(errors) < 0:
        return w
    print('Errors = ' + str(errors), end='\n\n')
    
    errors = np.array(errors)
    # Updating the w
    for ind, error in enumerate(errors):
        w = w + n*(error_label_real[ind]*2)*error
    
    return batch_perceptron(w, iteration=iteration)

batch_perceptron(np.array((1, 0, 0)), iteration=0)
