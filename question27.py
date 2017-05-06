import math

def isPrime(n):
    if n <= 0:
        return  False
    for k in range(2, math.ceil(n/2)):
        if n%k == 0:
            return False
    return True

bd = 1000
list_a = range(-bd + 1, bd)
list_b = [k for k in range(1, bd + 1) if isPrime(k)] #confine the possibility by using initial condition where n = 0
pairs = [[a, b] for b in list_b for a in list_a]
n = 0
while(1):
    if len(pairs) == 1:
        a = pairs[0][0]
        b = pairs[0][1]
    temp = []
    for each in pairs:
        if isPrime(n**2 + each[0]*n + each[1]):
            temp.append(each)
    if temp == []:
        break
    pairs = temp[:]
    n += 1
# n starts from 0
n += 1
print('the number of generated prime number: ' + str(n))
print('a = ' + str(a))
print('b = ' + str(b))
print('a*b = ' +  str(a*b))