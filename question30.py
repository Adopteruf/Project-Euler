import numpy as np
import time

# locate the number and calculate the sum
def locate_calculate(n, min_digit, max_digit):
    S = 0
    for k in range(10 ** min_digit, 10 ** max_digit + 1):
        if k == 1:
            continue
        s = 0
        for x in str(k):
            s += int(x) ** n
        if s == k:
            S += k
    return S

# find the maximum possible digit and take 4 as the initial condition
def max_digit(n):
    digit = 4
    while(1):
        M_increase = (digit - 1) * (9 ** n - 1)
        if 10 ** digit > M_increase * digit:
            break
        digit += 1
    #current digit higher than the current value not have any satisfied values
    digit -= 1
    return digit

# find the minimum possible digit and take 4 as the initial condition
def min_digit(n):
    digit = 1
    while (1):
        M_increase = (digit - 1) * (9 ** n - 1)
        if 10 ** digit < M_increase * digit:
            break
        digit += 1
        # the digit lower than the current value not have any satisfied values
    digit += 1
    return digit

start = time.time()
n = 5
min_d = min_digit(n)
max_d = max_digit(n)
print(locate_calculate(n, min_d, max_d))
end = time.time()
print(str(end - start))