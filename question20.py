# 2 lines in python
factorial = lambda x: 1 if x == 0 else x*factorial(x - 1)
result = sum([int(k) for k in str(factorial(100))])