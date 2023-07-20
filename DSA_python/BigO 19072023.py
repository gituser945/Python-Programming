# non domination term

def print_items(n):
    for i in range(n):
        for j in range(n):
            print(i,j)    # complexity O(n^2)
    for k in range(n):
        print(k)          # complexity O(n)

print_items(10)

# total complexity O(n^2 + n)
# drop the non dominating term which is n here so total complexity O(n^2)


# complexity O(n)

def sum(n):
    if n <= 0:
        return 0
    return n + sum(n-1)

sum(3)

# complexity O(1)

def pair_sum_sequence(n):
    total = 0
    for i in range(n):
        total = total + pair_sum(i,i+1)
    return total 

def pair_sum(a,b):
    return a+b

# Add vs Multiply 

def print_items(a,b):
    for i in range(a): 
        print(i)        # complexity O(a)
    for j in range(b):
        print(j)        # complexity O(b)
    
# total complexity O(a + b)

def print_items(a,b):
    for i in range(a):        # complexity O(a)
        for j in range(b):
            print(i,j)        # complexity O(b)
    
# total complexity O(a * b)
