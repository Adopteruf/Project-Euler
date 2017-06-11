n = 1
mark = 0
while(1):
    if 10**(n-1) > 9**n:
        break
    x = 9
    while(1):
        if x**n < 10**(n-1):
            break
        mark += 1
        x -= 1
    n += 1
print(mark)