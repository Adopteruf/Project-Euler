from itertools import permutations

x = range(1, 101)
per_2_x = permutations(x, 2)
f = lambda x,y: sum([int(k) for k in str(x**y)])
print(max([f(x[0],x[1]) for x in per_2_x]))