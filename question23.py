import math
import numpy as np
import time
start = time.time()
find_divisor = lambda num: [k for k in np.arange(1, num) if num%k == 0]
isAbundantNumber = lambda num: 1 if sum(find_divisor(num)) > num else 0
upper_bound = 28123
AN = np.array([k for k in np.arange(12, upper_bound + 1) if isAbundantNumber(k)])
s = 0
l = []
for k in np.arange(1, upper_bound + 1):
    rest = k - AN[:]
    rest = np.array([y for y in rest if y >= 0])
    mark = 1
    for x in rest:
        temp = [z for z in AN if x == z]
        if temp != []:
            mark = 0
            break
    s += mark*k
end = time.time()
print(end - start)
print(s)