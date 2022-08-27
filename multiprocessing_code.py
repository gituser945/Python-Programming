import time
from ast import arg
import multiprocessing


def square_number(numbers):
    for i in numbers:
        time.sleep(6)
        print('square',i*i)



def cube_number(numbers):
    for i in numbers:
        time.sleep(6)
        print('cube',i*i*i)


if __name__ == "__main__":
    
    arr = [1,2,3,4,5]

    p1 = multiprocessing.Process(target=square_number,args=(arr,))
    p2 = multiprocessing.Process(target=cube_number,args=(arr,))

    p1.start()
    p2.start()

    p1.join()
    p2.join()

    print("Done!!!!!")


