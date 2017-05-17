from functools import reduce
import math

digit_number = lambda n: int('9'*n) - 10**(n - 1) + 1
n, mark, s = 1, 0, []
for k in range(1, 6):
    while(1):
        num_th = 10**k
        current = n*digit_number(n) # compute the total digit's number in n digit integer
        if mark + current >= num_th:
            temp = int('9'*(n - 1)) + math.floor((num_th - mark)/n)
            s.append(int((str(temp)[-1] + str(temp + 1))[(num_th - mark)%n]))
            break
        mark += current # add up the current state
        n += 1
multi_product = reduce(lambda x,y: x*y, s)
print(multi_product)