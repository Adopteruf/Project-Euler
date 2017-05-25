num = 577
den = 408
mark = 0
for k in range(8, 1001):
    num += 2*den
    den = num - den
    if len(str(num)) > len(str(den)):
        mark += 1
print(mark)