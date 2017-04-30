# find the first day in months and judge them
def locate(start, end):
    firstMonths = [1]
    for k in range(start, end + 1):
        if k%100 == 0: # judge the type of a year
            bol = 1 if k%400 == 0 else 0
        else:
            bol = 1 if k%4 == 0 else 0
        Months = [31, 28 + bol, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
        for m in range(0, len(Months)): # find the date of the first day in months by years
            firstMonths.append(Months[m] + firstMonths[-1])
    valid = [date for date in firstMonths if date%7 == 0]
    return valid

valid = locate(1900, 2000)
day_in_1900 = sum([31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31])
valid = [date for date in valid if date > day_in_1900]
num = len(valid)
print(num)