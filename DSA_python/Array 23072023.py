#--------------- insertion of item into array ----------------

import array

my_array = array.array('i',[1,2,3,4,5])
print(my_array)
my_array.insert(0,6)
print(my_array)

# In this case time complexity O(N) and space complexity O(1)

#-------------------- Array traversal ------------------------

def array_traversal(arr):
    for i in arr:
        print(i)

arr = array.array('i',[10,9,4,2,5,1,5])
array_traversal(arr)

# In this case time complexity O(N) and space complexity O(1)

#------------------ Access elements of the array ------------

import array

arr = array.array('i',[1,2,3,4,5,6,7,8,9])

def accessElement(arr,index):
    if index >= len(arr):               #----> O(1)
        print("Out of range exception") 
    else:
        print(arr[index])               #----> O(1)

accessElement(arr,5)
accessElement(arr,9)

# In this case time complexity O(1) and space complexity O(1)

#------------------ Searching elements in the array ------------
import array

arr = array.array('i',[10,20,30,40,99])

def linearSearch(array,item):
    for i in range(len(array)): #------> O(n)
        if array[i] == item:    #------> O(1)
            return i            #------> O(1)
    return -1                   #------> O(1)

linearSearch(arr,99)
linearSearch(arr,100)

arr.index(99)

# In this case time complexity O(n) and space complexity O(1)


#------------------ Deleting elements from array --------------

import array

arr = array.array('i',[44,6,45,3,7])

def deleteItem(array,item):
    for i in range(len(array)):
        if array[i] == item:
            array.remove(item)
            return array
    return -1

print(arr)
deleteItem(arr,44)

# In this case time complexity O(n) except the last element with O(1)
# and space complexity O(1)

