#!/usr/bin/env python
# coding: utf-8

# In[3]:


from __future__ import print_function

import numpy as np
import matplotlib.pyplot as plt
import matplotlib.cm as cm

colors = cm.rainbow(np.linspace(0, 1, 10))


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
print(train_data.shape, train_labels.shape)


# In[13]:


def gradient_descent(x,n=0.00001,iterations = 1000):
    errors = []
    temp = np.random.random((784,2))
    u,d,v_t = np.linalg.svd(temp)
    v = u[:,:2]
    
    for i in range(iterations):
        T_0 = (np.dot(np.dot(x, v), v.T) - x)
        T_2 = (np.dot(np.dot(v, v.T), x.T) + -x.T)
        t_1 = np.linalg.norm(T_0, 'fro')
        gradient = (((1 / np.linalg.norm(T_2, 'fro')) * np.dot(np.dot(x.T, T_0), v)) + ((1 / t_1) * np.dot(np.dot(T_2, x), v)))
        errors.append(np.linalg.norm(T_0))
        v = v - n * (gradient + v)
#         print(v)
    plt.plot(errors)
    plt.savefig('3_errors.png')
    return v


# In[5]:


train_data = train_data - np.mean(train_data,axis=0)
v_grad = gradient_descent(train_data)


# In[6]:


data_grad = np.dot(train_data,v_grad)
for i in range(10):
    plt.scatter(data_grad[:,0][train_labels == i],data_grad[:,1][train_labels == i],color=colors[i])
plt.savefig('3_grad.png')


# In[10]:


def gradient_descent_1(x,n=0.00001,iterations = 1000):
    errors = []
    temp = np.random.random((784,2))
    u,d,v_t = np.linalg.svd(temp)
    v = u[:,:2]
    
    for i in range(iterations):
        T_0 = (np.dot(np.dot(x, v), v.T) - x)
        T_2 = (np.dot(np.dot(v, v.T), x.T) + -x.T)
        t_1 = np.linalg.norm(T_0, 'fro')
        gradient = (((1 / np.linalg.norm(T_2, 'fro')) * np.dot(np.dot(x.T, T_0), v)) + ((1 / t_1) * np.dot(np.dot(T_2, x), v)))
        errors.append(np.linalg.norm(T_0))
        v = v - n * (gradient + np.sign(v))
#         print(v)
    plt.plot(errors)
    plt.savefig('2_errors.png')
    return v


# In[11]:


v_grad_1 = gradient_descent_1(train_data)


# In[12]:


data_grad_1 = np.dot(train_data,v_grad_1)
for i in range(10):
    plt.scatter(data_grad_1[:,0][train_labels == i],data_grad_1[:,1][train_labels == i],color=colors[i])
plt.savefig('3_grad_1.png')


# In[ ]:




