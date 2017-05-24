def main():
    mark = 0
    for k in range(1, 10000):
        temp = k
        for j in range(0, 50):
            temp = temp + int(str(temp)[::-1])
            if str(temp) == str(temp)[::-1]:
                mark += 1
                break
    print(10000 - mark - 1)

main()