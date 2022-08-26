
import time

def time_it(func):
    def wrapper(*args,**kwargs):
        start = time.time()
        result = func(*args,**kwargs)
        end = time.time()
        print(func.__name__ + "took = " + str((end-start)*1000))
        return result
    return wrapper

@time_it # decorator of time
def square_fun(numbers):
    result = []
    for number in numbers:
        result.append(number*number)
    return result

@time_it # decorator of time
def cube_fun(numbers):
    result = []
    for number in numbers:
        result.append(number*number*number)
    return result

array = range(1,10000)
square_fun(array)
cube_fun(array)