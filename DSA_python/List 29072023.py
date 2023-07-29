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

