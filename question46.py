# Goldbach's other conjecture
# In this time, locating the prime number and composite_odd number is the first things
# Then we can enumerate that
import math
import time

def find_primes(n):
    primes = [True]*(n + 1)
    primes[0], primes[1] = False, False
    for k in range(1, n + 1):
        if primes[k]:
            for i in range(2*k, n + 1, k):
                primes[i] = False
    return primes

def find_composite_odd(n):
    c_odd = [False]*(n + 1)
    for k in range(3, n + 1, 2):
        for i in range(k*k, n + 1, k*2):
            c_odd[i] = True
    return c_odd


def main():
    n = 10 ** 6
    c_odd = find_composite_odd(n)
    primes = find_primes(n)
    sq_num = lambda x, prime: math.sqrt((x - prime)/2)
    for x, item in enumerate(c_odd):
        if item == False:
            continue
        boolean = 0
        for k in range(x, 2, -1):
            if primes[k]:
                temp = sq_num(x, k)
                if temp == int(temp):
                    boolean = 1
                    break
        if boolean == 0:
            print(x)
            break
start = time.time()
main()
end = time.time()
print(end - start)