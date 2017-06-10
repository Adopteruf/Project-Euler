# this algorithm actually does not solve the problem exactly. It is the manual adjustment of the range find the answer.

import math
import time

start = time.time()

def isPrime(num):
    for k in range(2, int(math.sqrt(num))):
        if num % k == 0:
            return False
    return True

def find_primes(n):
    primes = [True]*(n + 1)
    primes[0], primes[1] = False, False
    for k in range(1, n + 1):
        if primes[k]:
            for i in range(2*k, n + 1, k):
                primes[i] = False
    return primes

def isValid(a, b):
    str1 = str(a)
    str2 = str(b)
    if not isPrime(int(str1 + str2)):
        return False
    if not isPrime(int(str2 + str1)):
        return False
    return True

# recursive iteration
def find_result(primes_test, times, s):
    for ind, each in enumerate(primes_test):
        temp = [k for k in primes_test[ind+1:] if isValid(k, each) and isValid(each, k)]
        if temp == []:
            continue
        if times == 4:
            end = time.time()
            print(end - start)
            print(s+each+temp[0])
            exit()
        find_result(temp, times+1, s+each)

def main():
    fp = lambda N: [ind for ind, item in enumerate(find_primes(N)) if item]
    primes_test = fp(10**4)
    find_result(primes_test, times=1, s=0)
main()