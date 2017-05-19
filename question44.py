# Pentagon numbers
import math
import time

def main():
    start = time.time()
    Pentagon = lambda n: n*(3*n - 1)/2
    A = lambda n1, n2: n1 * (3*n1 - 1) + n2*(3*n2 - 1)
    B = lambda n1, n2: n2 * (3*n2 - 1) - n1*(3*n1 - 1)
    root = lambda x: (1 + math.sqrt(1 + 6*x))/6
    n2 = 5
    while (1):
        for n1 in range(1, n2):
            x = root(A(n1, n2))
            y = root(B(n1, n2))
            if int(x) == x and int(y) == y:
                print('n1: ' + str(n1))
                print('x: ' + str(x))
                print('y: ' + str(y))
                print('Pentagon: ' + str(Pentagon(n1)))
                end = time.time()
                print(end - start)
                exit()
        n2 += 1
main()