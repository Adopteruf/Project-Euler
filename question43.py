from itertools import permutations
import math
import numpy as np
import time

def locate_repeate_in_integer(arr):
    f = lambda x: 0 if len(set([k for k in str(x)])) != len(str(x)) else 1
    return np.array([f(x) for x in arr])

def divisible_three_digit(n):
    arr = np.arange(math.ceil(100/n), math.ceil(999/n))*n
    return np.delete(arr, np.where(locate_repeate_in_integer(arr) == 0))

def add_up(per_element, str_first3):
    s = 0
    for x in per_element:
        str_temp = ''.join(x)
        str_temp = str_temp[0] + str_first3 + str_temp[1:]
        boolean = True
        for k in range(2, 8):
            if int(str_temp[k:k+3]) % divide[k-1] != 0:
                boolean = False
                break
        if boolean:
            s += int(str_temp)
    return s

start = time.time()
elements = np.array(['0','1','2','3','4','5','6','7','8','9'])
divide = [2,3,5,7,11,13,17]
# consider the first part first to reduce the computations' number
d = divisible_three_digit(2)
s = 0
for x in d:
    temp = np.delete(elements, [int(str(x)[0]), int(str(x)[1]), int(str(x)[2])])
    per_element = list(permutations(temp, 7))
    s += add_up(per_element, str(x))

end = time.time()
print(end - start)
print(s)