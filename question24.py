import math
import numpy as np
import time

def factorial(num):
    if num == 0:
        return 1
    if num == 1:
        return 1
    return num*factorial(num - 1)

def locate_digit(left, local_upper):
    s = 0
    N = len(left)
    temp = factorial(N - 1)
    for x in left:
        s += temp
        digit = str(x)
        if len(left) == 1:
            return digit
        if s >= local_upper:
            # shrink the possible scale by iterations
            digit += locate_digit(np.delete(left, np.where(left == x)[0][0]), local_upper - (s - temp))
            return digit

start = time.time()
digit = locate_digit(np.array([0,1,2,3,4,5,6,7,8,9]), 10**6)
end = time.time()
print(str(end - start))
print(digit)