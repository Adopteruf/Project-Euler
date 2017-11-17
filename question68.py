import numpy as np
from itertools import permutations
ten_per = list(permutations([1,2,3,4,5,6,7,8,9,10], 10))
A = np.array(
    [np.array([1,1,0,0,0,1,0,0,0,0]),
     np.array([0,1,1,0,0,0,1,0,0,0]),
     np.array([0,0,1,1,0,0,0,1,0,0]),
     np.array([0,0,0,1,1,0,0,0,1,0]),
     np.array([1,0,0,0,1,0,0,0,0,1])])
for per in ten_per:
    cur_per = np.array(per)
    if min(cur_per[5:]) != cur_per[5]:
        continue
    if max(cur_per[5:]) != 10:
        continue
    production = np.sum(A*np.array(cur_per), 1)
    if len(np.unique(production)) != 1:
        continue
    cur_str_array = [str(each) for each in cur_per[[5,0,1,6,1,2,7,2,3,8,3,4,9,4,0]]]
    cur_str = ''.join(cur_str_array)
    print(cur_str)
