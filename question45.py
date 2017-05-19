# Triangular, pentagonal, and hexagonal
import math
Tri = lambda n: n*(n + 1)/2
root_p = lambda x: (1 + math.sqrt(1 + 12*Tri(x)*2))/6
root_h = lambda x: (1 + math.sqrt(1 + 8*Tri(x)))/4
n = 286
while(1):
    p = root_p(n)
    h = root_h(n)
    if int(p) == p and int(h) == h:
        print(Tri(n))
        break
    n += 1