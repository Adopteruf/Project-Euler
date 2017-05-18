from itertools import permutations
import math

def isPrime(num):
    for k in range(2, math.floor(math.sqrt(num) + 1)):
        if num % k == 0:
            return False
    return True

elements = ['1','2','3','4','5','6','7','8','9']
temp = 0
for n in range(4, 10):
    per_ele = [int(''.join(k)) for k in permutations(elements[0:n], n)]
    print(n)
    for x in per_ele:
        if isPrime(x):
            temp = x
print(temp)