# create an array and traverse

import array

arr = array.array('i',[1,2,3,4,5,6])
for i in arr:
    print(i)

# Access individual elements using indexes

arr[2]

# Append any value to array using append function

print(arr)
arr.append(10)
print(arr)

# insert value in an array using insert method

print(arr)
arr.insert(0,100)
print(arr)

# Extend array using extend() function

print(arr)
arr.extend([200,300,400])

# Add items from list into array using fromlist() method

lst = [111,222,333]
arr.fromlist(lst)
print(arr)


# Remove any array elements using remove() method

print(arr)
arr.remove(333)
print(arr)

# remove last array item using pop()

print(arr)
arr.pop()
print(arr)

# Fetch any elements through its index using index()

print(arr)
arr.index(1)

# reverse a python string using reverse()

arr.reverse()
print(arr)

# Get array buffer information using buffer_info() method

arr.buffer_info()

# Check for number of occurence of an element using count() method

print(arr)
arr.count(100)

# convert array to string using tostring() method

arr = arr.tostring()

# convert same string using tolist

ints = array.array('i')
ints.fromstring(arr)
ints

# slice elements from array

ints[4:7]



