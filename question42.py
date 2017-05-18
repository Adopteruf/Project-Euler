import math

f = lambda x: ((1 + math.sqrt(1 + 8*x))/2)
isInteger = lambda x: 1 if int(x) == x else 0

file = open('E:\CodesPackage-notes\Python\Project-Euler\p042_words.txt','r')
text = file.read()
file.close()
text = text[1:-1]
words = text.split('","')
mark = 0
for x in words:
    num = sum([ord(y.upper()) - ord('A') + 1 for y in x.upper()])
    if isInteger(f(num)):
        mark += 1
print(mark)