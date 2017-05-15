def array(n):
    arr = [n]
    str_n = str(n)
    for x in range(1, len(str_n)):
        arr.append(int(str_n[:x]))
        arr.append(int(str_n[x:]))
    return arr

def find_prime(n):
    pl = [True] * n
    pl[0], pl[1] = False, False
    for y in range(0, n):
        if pl[y]:
            # find the non-prime number is more easy and fast
            for x in range(2 * y, n, y):
                pl[x] = False
    return pl

def main():
    mark, s = 0, 0
    pls = find_prime(10 ** 6)
    exam = lambda x: 1 if pls[x] else 0
    for idx, item in enumerate(pls):
        if idx <= 10:
            continue
        if mark == 11:
            break
        if item:
            if list(map(exam, array(idx))).count(0) == 0:
                mark += 1
                s += idx
    print(s)
    print(mark)
main()