# Distinct primes factors
# there is trick when locating the prime factor of a number
# the prime factor usually is made up of many small prime number and only one big prime number
# the time and computations spent on diving the base to the last one is huge
# Thus, we can automatically decide whether the next prime factor is the last huge one.
import time

def is_four_prime_factor1(n):
    base = 2
    count = 0
    # when the base^2 < n, as base increase by steps, n is a prime number
    while base**2 < n:
        while n%base:
            base += 1
        while not n%base:
            n //= base
        count += 1
    count += 1
    return count == 4

def main():
    fp = [False] * (10 ** 6 + 1)
    for x in range(1, 10 ** 6 + 1):
        fp[x] = is_four_prime_factor1(x)
        if x < 10:
            continue
        if fp[x] and fp[x - 1] and fp[x - 2] and fp[x - 3]:
            print(x - 3)
            break
start = time.time()
main()
end = time.time()
print(end - start)