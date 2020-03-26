# -*- coding: utf-8 -*-
"""
Created on Wed Mar 25 22:56:21 2020

@author: Beejal
"""

import numpy as np

l = [1, 2, 3, 4]
print(type(l))

l = np.array(range(1,10))
print('np.array()')
print(l)

#
print('Create a length-10 integer numpy-array filled with zeros')
print(np.zeros(10, dtype=int))
#
print('Create a length-10 integer numpy-array filled with ones')
print(np.ones(10, dtype=int))
#
print('Create a 3*5 numpy-array (2D) filled with value 3.14')
print(np.full((3, 5), 3.14))
#
## Create an array filled with a linear sequence
## Starting at 0, ending at 20, stepping by 2
## (this is similar to the built-in range() function)
print('Create a numpy-array from values 1-9')
print(np.arange(0, 20, 2))
#
#
print('Create a numpy-array of five values evenly spaced between 0 and 1')
print(np.linspace(0, 1, 5))
#
print('Create a 3x5 numpy-array of uniformly distributed random values between 0 and 1')
print(np.random.random((3, 5)))
#
#print('Create a 4x5 numpy-array from normal distribution with mean 0 and std-deviation 1')
data = np.random.normal(0, 1, (4, 5))
print(data)
#
print('Create a numpy array of random integers with high value of 10 and low value of 6')
print(np.random.randint(low=6, high=10, size=10))
#
print('Create a numpy 2-D array of size 2*3 containing integers, when low alone is given it is considered as high')
print(np.random.randint(low=10, size=(2, 3)))
#
#
np.random.seed(0) # seed for reproducibility
x1 = np.random.randint(10, size=6) # One-dimensional array
x2 = np.random.randint(10, size=(3, 4)) # Two-dimensional array
x3 = np.random.randint(10, size=(3, 4, 5)) # Three-dimensional array

print(x1)

#
print('Attributes of numpy-array:')
print('x3::\n', x3)
print('ndim (the number of dimensions) ', x3.ndim)
print('shape (the size of each dimension) ', x3.shape)
print('size (total size of array) ', x3.size)
print('dtype (data type of array) ', x3.dtype)
print('itemsize (bytes for each item) ', x3.itemsize)
print('nbytes (total size, in terms of bytes, of the array ', x3.nbytes)
#
#
print('Array Indexing')
print('x1::\n', x1)
print('Access the last element of array')
print(x1[-1])
print(x1[-2])
print(x1[0])
print(x1[0:-2])

print()
print('x2::\n', x2)
print(x2[0][0])
print(x2[0][2])
print(x2[1][-1])
#
x2[1][-1] = 10
print('x2::\n', x2)
#
x2[0][1] = 3.9 # this will be truncated!
print('x2::\n', x2)
#
