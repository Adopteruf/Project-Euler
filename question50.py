import time

def find_primes(n):
    primes = [True]*(n + 1)
    primes[0], primes[1] = False, False
    for k in range(1, n + 1):
        if primes[k]:
            for i in range(2*k, n + 1, k):
                primes[i] = False
    primes = [idx for idx, item in enumerate(primes) if item]
    return primes

# start from the largest length of sequence
def main():
    start = time.time()
    n = 1000000
    primes = find_primes(n)
    min_bdd = 23
    s = 0
    for idx, item in enumerate(primes):
        s += item
        if s >= n:
            max_bdd = idx
            break
    for seq_length in range(max_bdd, min_bdd, -1):
        for k in range(0, n - seq_length):
            temp_sum = sum(primes[k: k + seq_length])
            if temp_sum >= n:
                break
            if primes.count(temp_sum) >= 1:
                print(seq_length)
                print(k)
                print(sum(primes[k:k + seq_length]))
                end = time.time()
                print(end - start)
                exit()
main()