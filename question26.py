# using long division to check the reminders
def determine_period(num):
    length = len(str(num))
    divider = 10 ** length
    rems = []
    period = 0
    while(1):
        reminder = divider % num
        if reminder == 0:
            return 0
        if rems.count(reminder) != 0:
            return period
        period += 1
        rems.append(reminder)
        divider = reminder * 10 ** length

periods = [determine_period(k) for k in range(1, 1000 + 1)]
locate = periods.index(max(periods))
print(locate + 1)