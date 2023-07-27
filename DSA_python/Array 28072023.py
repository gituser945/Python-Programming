# working with two dimensinal array

import numpy as np

my_array = np.array([[10,11,12,13],[11,22,55,33],[111,222,555,333],[1,2,3,4]])

print(my_array)

# traversing through 2-d array

def twodimensional(array):
    for i in range(len(array)):         #---> O(mn)
        for j in range(len(array)):     #---> O(n)
            print(array[i][j])          #---> O(1)

twodimensional(my_array)

# time complexity = O(n^2) and space complexity is O(1)

# searching for value in 2D array uning linear search

def twodimensionalsearch(array,item):
    for i in range(len(array)):         #---> O(mn)
        for j in range(len(array)):     #---> O(n)
            if array[i][j] == item:     #---> O(1)
                return i,j
    return 'element not found'

twodimensionalsearch(my_array,4)
twodimensionalsearch(my_array,222)
twodimensionalsearch(my_array,21)

# time complexity = O(n^2) and space complexity is O(1)
