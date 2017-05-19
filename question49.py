# Here comes mostly the thoughts on manipulate the vectors or matrix
import numpy as np
import time

def find_primes(n):
    primes = [True]*(n + 1)
    primes[0], primes[1] = False, False
    for k in range(1, n + 1):
        if primes[k]:
            for i in range(2*k, n + 1, k):
                primes[i] = False
    return primes

def isValid(current):
    for k in range(0, len(current) - 2):
        each = current[k]
        boolean = True
        for x in range(0, 2):
            each += 3330
            if not current.count(each):
                boolean = False
                break
        if boolean:
            return True, str(each - 2*3330) + str(each - 3330) + str(each)
    return False, None

def main():
    get_str_in_order = lambda n: ''.join(sorted([str(n)[0], str(n)[1], str(n)[2], str(n)[3]]))

    primes = np.array([idx for idx, item in enumerate(find_primes(9999)) if item and idx > 999])
    normal_str_primes = np.array([get_str_in_order(x) for x in primes])
    unique_normal_str_primes = set(normal_str_primes)
    for each in unique_normal_str_primes:
        temp_index = np.where(normal_str_primes == each)[0]
        current = [primes[k] for k in temp_index]
        if len(current) < 3 or current[-1] - current[0] < 3330*2:
            continue
        boolean, result = isValid(current)
        if boolean:
            print(result)
start = time.time()
main()
end = time.time()
print(end - start)