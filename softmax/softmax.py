import numpy as np

# Write a function that takes as input a list of numbers, and returns
# the list of values given by the softmax function.
def softmax(L):
    exp_values = np.exp(L - np.max(L))  
    return exp_values / np.sum(exp_values)