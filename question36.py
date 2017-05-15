dec2bin_str = lambda x: bin(x).replace('0b', '')
# bin2dec = lambda x: int(str(x), base = 2)
test1 = lambda k: 1 if (int(str(k)[::-1]) == k) else 0
test2 = lambda k: 1 if (int(dec2bin_str(k)[::-1]) == int(dec2bin_str(k))) else 0
print(sum([k for k in range(1, 10 ** 6) if test1(k) and test2(k)]))