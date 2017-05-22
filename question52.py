# Permuted multiples
import time

start = time.time()
x = 1
keys = [2,3,4,5,6]
while True:
    boolean = True
    if len(str(x*6)) != len(str(x)):
        # jump the numbers with same number of digit
        x = 10**(len(str(x)))
    t1 = x
    for each in keys:
        t2 = x*each
        if set([str(m) for m in str(t1)]) != set([str(k) for k in str(t2)]):
            boolean = False
            break
        t1 = t2
    if boolean:
        print(x)
        end = time.time()
        print(end - start)
        exit()
    x += 1