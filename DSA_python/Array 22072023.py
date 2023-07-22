# creating array using array module

import array

my_array = array.array('i',[1,2,44,55,10]) # time complexity O(n) # space complexity O(n)
print(my_array)

# create array using numpy

import numpy as np

np_array = np.array([],dtype=int) # empty array
print(np_array)

np_array = np.array([1,2,3,4,5,6]) # time complexity O(n) # space complexity O(n)
print(np_array)
