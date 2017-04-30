l = []
for x in range(2, 10000):
    b = sum([y for y in range(1, x) if x%y == 0])
    l.append([x,b])
l = [str(sorted(k)[0]) +'+'+str(sorted(k)[1]) for k in l] # reduce two ints to one string
l = set([k for k in l if l.count(k) > 1])
print(sum([eval(k) for k in l]))
