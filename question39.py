import math

T = 1000
s = [0] * (T + 1)
for Top in range(1, T + 1):
    mark = 0
    # kernel but simple formula
    f = lambda x: Top - (Top ** 2) / (2 * (Top - x))
    for x in range(1, math.ceil(Top / 2)):
        if f(x) == int(f(x)):
            mark += 1
    s[Top] = mark
print(s.index(max(s)))
print(max(s))