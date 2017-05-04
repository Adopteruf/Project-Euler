def fibonacci(n):
    if n == 1 or n == 2:
        return 1
    return fibonacci(n - 1) + fibonacci(n - 2)

x = 1
y = 1
mark  = 2
while(1):
    temp = x + y
    x = y
    y = temp
    mark += 1
    if (len(str(y)) == 1000):
        break
print(mark)