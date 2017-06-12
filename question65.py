from fractions import Fraction
import math

n = 99
base = [2] + [1]*n
for k in range(0, math.floor(n/3)): base[2+3*k] = 2*(k+1)
f = Fraction(1, base[-1])
for each in base[:-1][::-1]:
    f = each + 1/f
print(sum([int(k) for k in str(f.numerator)]))