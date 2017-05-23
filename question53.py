# Combinatoric selections
factorial = lambda n: 1 if n == 1 or n == 0 else n*factorial(n - 1)
combinations = lambda n,k :1 if n == k else factorial(n)/(factorial(k) * factorial(n - k))

mark = 0
for x in range(10, 101):
    for y in range(1, x + 1):
        temp = combinations(x, y)
        if temp > 1000000:
            mark += 1
print(mark)