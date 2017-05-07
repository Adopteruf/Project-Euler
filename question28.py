locate = lambda x, n: x + (4 * n - 4) - 1 # locate the leftest and the most top value in n*n matrix
calculate_sum = lambda x, n: sum(range(x, x - 3 * (n - 1) - 1, - (n - 1))) # calculate the sum of four corners in n*n matrix
x0 = 2
s = 1
n = 1001
for k in range(3, n + 1, 2):
    x1 = locate(x0, k)
    s += calculate_sum(x1, k)
    x0 = x1 + 1
print(s)