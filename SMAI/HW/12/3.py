import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv('faults.csv')

train_data = data[:100]
train_mean = train_data.mean(axis=0)
train_var = train_data.var(axis=0)
train_data = (train_data - train_mean)/train_var.apply(np.sqrt)

test_data = data[:100]

train_labels = data[:100]['Other_Faults']
test_labels = data[100:]['Other_Faults']

def hessian(x):
    '''
    x is the array
    '''
    x_grad = np.gradient(x)
    hessian = np.empty((x.ndim, x.ndim)+x.shape, dtype=x.dtypes)

    for k, grad_k in enumerate(x_grad):
        tmp_grad = np.gradient(grad_k)
        for l, grad_kl in enumerate(tmp_grad):
            hessian[k, l, :, :] = grad_kl
    
    return hessian

hess = hessian(train_data)

def grad_desc(x, eta=0.5, epsilon=1e-4):
    w_init = np.zeros(x.shape[1])
    w_new = np.ones(x.shape[1])
    
    count = 0
    while np.linalg.norm(w_new - w_init) > epsilon:
        
        s = np.zeros(x.shape[1])
        for i in range(train_labels):
            s1 = train_labels[i] - np.dot(w_new, train_data[i])
            s1 = (-1) * s1 * train_data[i]
            s += s1
            
        del_J = (2 / len(train_data)) * s
        w_init = w_new
        w_init -= eta * del_J
        
        if count > 1000:
            break
            
    return w_init


