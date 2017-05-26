# range() is highly time-costing
# find_primes in list first is not necessary the best method
import math
import time

def isPrime(num):
    if num <= 1:
        return False
    for k in range(2, math.floor(math.sqrt(num))):
        if num % k == 0:
            return False
    return True

start = time.time()
num_base = 1
pr_base = 0
inside_diff = 2
outside_diff = 4
t = 3
while(1):
    pr_base += isPrime(t)
    pr_base += isPrime(t + inside_diff)
    pr_base += isPrime(t + 2*inside_diff)
    t = t + 3*inside_diff + outside_diff
    if pr_base/(4*inside_diff/2) < 0.1:
        print(inside_diff + 1)
        end = time.time()
        print(end - start)
        exit()
    inside_diff += 2
    outside_diff += 2