# program without multithreading

import threading
import time 

def square_number(numbers):
    for n in numbers:
        time.sleep(0.2)
        print('square',n*n)


def cube_number(numbers):
    for n in numbers:
        time.sleep(0.2)
        print('cube',n*n*n)


arr = [2,4,6,8]

t = time.time()

#square_number(arr)
#cube_number(arr)

t1 = threading.Thread(target=square_number,args=(arr,))
t2 = threading.Thread(target=cube_number,args=(arr,))

t1.start()
t2.start()

t1.join()
t2.join()

print(f'time taken :{(time.time()-t)}')

