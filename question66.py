# Pell's equation and continued fraction help solve this
import math

def initialize(x):
    r = int(math.floor(math.sqrt(x)))
    return r, x, r, 1

def process(x, r, de, max):
    # (x^(1/2) - r)/d
    # (x^(1/2) + R)/D
    R = r
    D = int((x - r**2)/de)
    de = D
    a = 1
    while(1):
        if math.fabs(R - a*D) > max:
            a -= 1
            r = -(R - a*D)
            break
        a += 1
    return a, x, r, de

def locate_x(D):
    a0, x, r, de =  initialize(D)
    MAX = a0
    h1 = 1
    k1 = 0
    h2 = a0*1 + 0
    k2 = a0*0 + 1
    while(1):
        a, x, r, de = process(x, r, de, MAX)
        if h2**2 - D*k2**2 == 1:
            return h2
        temp_h2 = h2
        temp_k2 = k2
        h2 = a*h2 + h1
        k2 = a*k2 + k1
        h1 = temp_h2
        k1 = temp_k2

def main():
    N = 1000
    L = [0]*(N+1)
    for D in range(1, N+1):
        if int(math.sqrt(D)) == math.sqrt(D):
            continue
        L[D] = locate_x(D)
    print(L.index(max(L)))

main()