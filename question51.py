# Prime digit replacements
import time

def find_primes(n):
    primes = [True]*(n + 1)
    primes[0], primes[1] = False, False
    for k in range(1, n + 1):
        if primes[k]:
            for i in range(2*k, n + 1, k):
                primes[i] = False
    return primes

def main():
    primes = find_primes(10**6)
    keys = [0, 1, 2]
    for id, item in enumerate(primes):
        if not item:
            continue
        temp_str = str(id)
        for each in keys:
            if temp_str.count(str(each)) == 0:
                continue
            mark = 1
            for k in range(each + 1, 10):
                if primes[int(temp_str.replace(str(each), str(k)))]:
                    mark += 1
            if mark == 8:
                print(temp_str)
                print(each)
                exit()

start = time.time()
main()
end = time.time()
print(end - start)