# Working with list

integer = [1,2,3,4]
print(integer)

stringList = ['tom','jack']
print(stringList)

mixedList = [1,2,3,1.5,'tom']
print(mixedList)

nestedList = [1,2,['tom',1.5],'sam']
print(nestedList)

emptyList = []
print(emptyList)

# accessing and traversing the list

shoppingList = ['Milk','Cheese','Butter']

def traverseList(array):
    for i in shoppingList:
        print(i)

traverseList(shoppingList)

# list 'in' operator

print('Milk' in shoppingList)

# return using index value

print(shoppingList[-1])

# Insert and Update the list

myList = [1,2,3,4,5,6]

def updateList(list,updateitem,updatevalue):
    for i in range(len(list)):
        if list[i] == updateitem:
            list[i] = updatevalue
    return list

print(myList)
updateList(myList,3,'updated value')

# Leetcode problem 1

sentences = ["alice and bob love leetcode", "i think so too", "this is great thanks very much"]

count = []
for i in range(len(sentences)):
    count.append(len(sentences[i].split()))
print(max(count))

count = len(sentences[0].split())

len(sentences[0].split())

# Leetcode problem 2

accounts = [[2,8,7],[7,1,3],[1,9,5]]

maxAmount = []
for i in range(len(accounts)):
    maxAmount.append(sum(accounts[i]))
print(max(maxAmount))

# Leetcode problem 3

nums = [3,1,2,10,1]

newList = []
j = 0
for i in range(len(nums)):
    j += nums[i]
    newList.append(j)

# Leetcode problem 4

nums = [8,1,2,2,3]

newList = []
maxElement = max(nums)
counter = 0
for i in range(len(nums)):
    if nums[i] > maxElement:
        counter += 1
        newList.append(counter)
print(newList)
