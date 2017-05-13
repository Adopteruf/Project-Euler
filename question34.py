factorial = lambda x: 1 if x == 1 or x == 0 else x * factorial(x - 1)

# locate the bound of digit's number first
def find_bdd():
    Max = 1
    while(1):
        if len(str(factorial(9) * Max)) < Max:
            Max -= 1
            break
        Max += 1
    Min = 2
    return Min, Max

# exam the validity of the number
def isValid(num):
    s = 0
    for x in str(num):
        s += factorial(int(x))
    return s == num

# do the iteration and calculations
def locate_calculate(Min, Max):
    s = 0
    for k in range(10 ** (Min - 1), 10 ** (Max - 1) + 1):
        if isValid(k):
            s += k
    return s

Min, Max = find_bdd()
print(locate_calculate(Min, Max))