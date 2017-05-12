from fractions import Fraction
# from fractions import gcd
from itertools import permutations

elements = ['1', '2', '3', '4', '5', '6', '7', '8', '9']
d_permutation = [k for k in permutations(elements, 2)]
d_elements = [''.join(k) for k in d_permutation]
for k in range(1, 10):
    d_elements.append(str(k) + str(k))
fraction_elements = [k for k in permutations(d_elements, 2)]
num = 1
den = 1
mark = 0
for x in fraction_elements:
    if mark == 4:
        break
    temp = Fraction(int(x[0]), int(x[1]))
    if temp.numerator/temp.denominator > 1:
        continue
    cnum = int(x[0][0]) * int(x[0][1])
    cden = int(x[1][0]) * int(x[1][1])
    frac = Fraction(cnum, cden)
    if frac != Fraction(int(x[0][0]), int(x[1][0])) and frac != Fraction(int(x[0][0]), int(x[1][1])) and frac != Fraction(int(x[0][1]), int(x[1][0])) and frac != Fraction(int(x[0][1]), int(x[1][1])):
        continue
    if frac == temp:
        num *= cnum
        den *= cden
        mark += 1

print(Fraction(num, den).denominator)