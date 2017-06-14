# dynamic programming
import time
start = time.time()
file = open('E:\CodesPackage-notes\Python\Project-Euler\q67.txt')
N = 100
arr = [[0]*N]*N
for ind, each in enumerate(file):
    temp = [int(k) for k in each[:].split(' ')]
    arr[ind] = temp + [0]*(N - len(temp))
s = [arr[0][0] + arr[1][0], arr[0][0] + arr[1][1]] + [0]*(N - 2)
c = s[:]
for k in range(2, N):
    c[0] = s[0] + arr[k][0]
    c[k] = s[k - 1] + arr[k][k]
    for b in range(1, k):
        c[b] = max([s[b - 1], s[b]]) + arr[k][b]
    s = c[:]
print(max(s))
end = time.time()
print(end - start)