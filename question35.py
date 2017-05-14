import math
import time

def circular_num(n):
    s = str(n)
    N = len(s)
    circular = [0] * (N - 1)
    for k in range(1, N):
        circular[k - 1] = int(s[k:N] + s[0:k])
    return circular

def find_prime(n):
    pl = [True] * n
    pl[0], pl[1] = False, False
    for y in range(0, n):
        if pl[y]:
            # find the non-prime number is more easy and fast
            for x in range(2 * y, n, y):
                pl[x] = False
    return pl

# slow method for judging each number.
def find_prime_slow(n):
    pl = [True] * n
    for x in range(0, n):
       if isPrime(x) != True:
           pl[x] = False
    return pl

def isPrime(num):
    for k in range(2, math.floor(math.sqrt(num) + 1)):
        if num % k == 0:
            return False
    return

def main():
    pl1 = find_prime(1000000)
    # pl2 = find_prime_slow(1000000)
    length = 0
    for (k, IsPrime) in enumerate(pl1):
        if IsPrime:
            length += 1
            circular = circular_num(k)
            for x in circular:
                if pl1[x] == False:
                    length -= 1
                    break
    print(length)

start = time.time()
main()
end = time.time()
print(str(end - start))