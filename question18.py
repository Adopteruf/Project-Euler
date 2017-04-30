# by using the dynamic programming calculate the result of possible routes from the top to the bottom
file = open('E:\CodesPackage-notes\Python\Project-Euler\q18.txt')
text = file.read()
file.close()
text = text.split('\n')
arr = []
for k in range(0, len(text)):
    arr.append([int(t) for t in text[k].split(' ')])
sum = [[arr[0][0]]] + [[] for k in range(0, len(text)-1)]
for k in range(1, len(text)):
    s = [[] for m in range(0, len(text))] # create the temp space for each iteration
    for j in range(0, k):
        if j == k:
            continue
        for n in range(0, len(sum[j])):
            s[j].append(sum[j][n] + arr[k][j])
            s[j+1].append(sum[j][n] + arr[k][j+1])
    sum = s[:] # update the current result for different routes
result = [max(list) for list in sum]
Max = max(result)
print('result:' + str(Max))