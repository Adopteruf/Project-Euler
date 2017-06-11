# use the dfs searching algorithm
from itertools import permutations
import time

start = time.time()
seq_generator = lambda f, n, N: [str(f(k)) for k in range(n, N+1)]

T = lambda n: n*(n+1)/2
S = lambda n: n**2
P = lambda n: n*(3*n-1)/2
HEX = lambda n: n*(2*n-1)
HEP = lambda n: n*(5*n-3)/2
O = lambda n: n*(3*n-2)
Seq1 = seq_generator(T, 45, 140)
Seq2 = seq_generator(S, 32, 99)
Seq3 = seq_generator(P, 26, 81)
Seq4 = seq_generator(HEX, 23, 70)
Seq5 = seq_generator(HEP, 21, 63)
Seq6 = seq_generator(O, 19, 58)
SEQ = [[], Seq1, Seq2, Seq3, Seq4, Seq5, Seq6]

def dfs(Seq, times, l, order):
    if times > 4:
        return
    base = SEQ[order[times + 1]]
    for each in Seq:
        temp = [x for x in base if each[2:] == x[0:2] and l.count(x) == 0]
        if temp == []:
            continue
        l[times] = each
        if times == 4 and l[0][0:2] == temp[0][2:]:
            l[-1] = temp[0]
            print(l, sum([int(k) for k in l]))
            print(order)
            end = time.time()
            print(end-start)
            exit()
        dfs(temp, times+1, l, order)
        l[times]='0'

def main():
    base = [1,2,3,4,5,6]
    per_base = permutations(base, len(base))
    for each in per_base:
        dfs(Seq=SEQ[each[0]], times=0, l=['0']*6, order=each)
main()