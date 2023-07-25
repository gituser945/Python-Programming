# working with two dimensional array

import numpy as np

two_dimensional = np.array([[11,15,10,6],
                            [10,14,11,5],
                            [12,17,12,8],
                            [15,18,14,9]])

print(two_dimensional)

two_dimensional = np.insert(two_dimensional,0,[[1,2,3,4]],axis=1) # axis = 1 (column), 0 as rows

print(two_dimensional)

two_dimensional = np.insert(two_dimensional,0,[[1,2,3,4,5]],axis=0)

print(two_dimensional)
len(two_dimensional)

# time complexity of this insertion in 2D array is O(mn)

# accessing element from 2 dimensional array

def accessElement(array,rowIndex,colIndex):
    if rowIndex >= len(array) or colIndex >= len(array): #----> O(1)
        print("Incorrect row or column index")           #----> O(1)
    else:
        return array[rowIndex][colIndex]                 #----> O(1)

accessElement(two_dimensional,3,2)
accessElement(two_dimensional,17,2)

# Time complexity is O(1) and space complexity is also O(1)
