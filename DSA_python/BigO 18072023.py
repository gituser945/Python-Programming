# Constant time complexity O(1)

def multiply_numbers(n):
    return n*n

print(multiply_numbers(5))
print(multiply_numbers(5000))

# Linear time complexity O(n)

def print_items(n):
    for i in range(n):
        print(i)

print_items(10)
print_items(100)

# O(2n)

def print_items(n):
    for i in range(n):
        print(i)
    for j in range(n):
        print(j)

print_items(10)
print_items(100)

# Order of n-square O(n^2)

def print_items(n):
    for i in range(n):
        for j in range(n):
            print(i,j)

print_items(10)
print_items(100)

# Order of n-qube O(n^3)

def print_items(n):
    for i in range(n):
        for j in range(n):
            for k in range(n):
                print(i,j,k)

print_items(10)
print_items(100)







