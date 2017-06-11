cute_generator = lambda N: [k**3 for k in range(1, N+1)]
cutes = cute_generator(10**5)
cutes_chr = [sorted([x for x in str(each)]) for each in cutes]
index = 0
for ind, each in enumerate(cutes_chr):
    if cutes_chr.count(each) == 5:
        index = ind
        break
print(cutes[index])