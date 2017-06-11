import math
import time
start = time.time()
list2str = lambda L:''.join([str(k)+'0' for k in L])

def initialize(x):
    r = int(math.floor(math.sqrt(x)))
    return r, x, r, 1

def process(x, r, de, max):
    # (x^(1/2) - r)/d
    # (x^(1/2) + R)/D
    D = int((x - r**2)/de)
    R = r
    de = D
    a = 1
    while(1):
        if math.fabs(R - a*D) > max:
            a -= 1
            r = -(R - a*D)
            break
        a += 1
    return a, x, r, de

def period(n):
    a0, x, r, de =  initialize(n)
    max = a0
    a0, x, r, de = process(x, r, de, max)
    a = a0
    L = list2str([x, r, de])
    times = 0
    while(1):
        a0, x, r, de = process(x, r, de, max)
        times += 1
        temp = list2str([x, r, de])
        if L == temp and a == a0:
            return times

def main():
    mark = 0
    for n in range(2, 10**4 + 1):
        if int(math.sqrt(n)) == math.sqrt(n):
            continue
        if period(n)%2:
            mark += 1
    print(mark)
    end = time.time()
    print(end - start)
main()