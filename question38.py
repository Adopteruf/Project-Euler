# type1 = [1, 2, 2, 2, 2] # 918273645
# type2 = [2, 3, 4] # invalid
# type3 = [3, 4, 2] # invalid
# type4 = [4, 5]

from itertools import permutations

elements = ['1', '2', '3', '4', '5', '6', '7', '8']
e_permutation = [k for k in permutations(elements, 8)]
cases = ['9' + ''.join(x) for x in e_permutation]
s = []
for y in cases:
    if int(y[4:]) / int(y[:4]) == 2:
        s.append(int(y))
print(max(s))