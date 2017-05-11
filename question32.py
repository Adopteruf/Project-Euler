from itertools import permutations
elements = ['1', '2', '3', '4', '5', '6', '7', '8', '9']
# all possible permutations
per = permutations(elements, 9)
s = []
for k in per:
        eq = ''.join(k)
        str1 = eq[0] + '*' + eq[1:5] + '==' + eq[5:-1] + eq[-1]
        str2 = eq[0:2] + '*' + eq[2:5] + '==' + eq[5:-1] + eq[-1]
        bol1 = eval(str1)
        bol2 = eval(str2)
        if bol1 or bol2:
            num = int(eq[5:-1] + eq[-1])
            if s.count(num) == 0:
                s.append(num)
print(sum(s))