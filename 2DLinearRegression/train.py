'''
This is a simple iterative procedure intended to illustrate how gradient descent works. Data is generated randomly,
based on a Guassian distribution, centered on a line. The model then attempts to find that line with linear regression.
'''

import pandas as pd
import numpy as np

# Gets train and test data
df_train = pd.read_csv('train.csv')
df_test = pd.read_csv('test.csv')

# Separate x value (feature) and y value (label)
x_train = df_train['x']
y_train = df_train['y']
x_test = df_test['x']
y_test = df_test['y']

# Transforms dataframe to array
x_train = np.array(x_train)
y_train = np.array(y_train)
x_test = np.array(x_test)
y_test = np.array(y_test)

# n is the number of training examples. alpha is the learning rate.
n = 1000
alpha = 0.0002

# The starting guess for the line of best fit (y = 1)
a_0 = 0
a_1 = 1

# Runs 100000 times
epochs = 0
while(epochs < 100000):
    # Calculate error per training example, which is the difference between the prediction and the actual value
    y = a_0 + a_1 * x_train
    error = y - y_train
    # Consolidate errors into mean squared error (for evaluation purposes)
    mean_sq_er = np.sum(error**2)
    mean_sq_er = mean_sq_er/n
    # Adjust the weigths according to the error
    a_0 = a_0 - alpha * np.sum(error)/n
    a_1 = a_1 - alpha * np.sum(error * x_train)/n
    epochs += 1
    # Every 10 steps, print out an evaluation
    if(epochs%10 == 0):
        print(epochs)
        print(mean_sq_er)
print(a_0)
print(a_1)
