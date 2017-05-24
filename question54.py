# this method follows the rule strictly and there must exists more smart way.
stand = ['2', '3', '4', '5', '6', '7', '8', '9', 'T', 'J', 'Q', 'K', 'A']

def rank(t):
    value = [each[0] for each in t]
    suit = [each[1] for each in t]
    is_same_suit = True if len(set(suit)) == 1 else False
    # Royal Flush: Ten, Jack, Queen, King, Ace, in same suit.
    if is_same_suit and value == ['T','J','Q','K','A']:
        return 10, None
    start = stand.index(value[0])
    is_consecutive = value == stand[start:start + 5]
    # Straight Flush: All cards are consecutive values of same suit.
    if is_same_suit and is_consecutive:
        return 9, None
    type = set(value)
    len_type = len(type)
    # Four of a Kind: Four cards of the same value.
    if len_type <= 2:
        for each in type:
            if value.count(each) >= 4:
                return 8, [each]
    type = list(type)
    # Full House: Three of a kind and a pair.
    if len_type == 2:
        if value.count(type[0]) == 2:
            return 7, [type[1]]
        if value.count(type[0]) == 3:
            return 7, [type[0]]
    # Flush: All cards of the same suit.
    if is_same_suit:
        return 6, None
    # Straight: All cards are consecutive values.
    if is_consecutive:
        return 5, value[-1]
    # Three of a Kind: Three cards of the same value.
    if len_type <= 3:
        for each in type:
            if value.count(each) == 3:
                return 4, [each]
    # Two Pairs: Two different pairs.
    if len_type == 3:
        temp = []
        for each in value:
            if value.count(each) == 2:
                temp.append(each)
        temp.sort(reverse = False)
        return 3, temp
    # One Pair: Two cards of the same value.
    if len_type == 4:
        temp = 0
        for each in value:
            if value.count(each) == 2:
                return 2, [each]
    return 1, None

def sorting(x, y):
    if stand.index(x[0]) > stand.index(y[0]):
        return 1
    if stand.index(x[0]) < stand.index(y[0]):
        return -1
    return 0

def compare(t1, t2):
    t1 = sorted(t1, cmp=sorting)
    t2 = sorted(t2, cmp=sorting)
    r1, temp1 = rank(t1)
    r2, temp2 = rank(t2)
    if r1 > r2:
        return 1
    if r1 < r2:
        return 0
    if r1 == r2:
        if temp1 != None:
            for k in range(0, len(temp1)):
                if stand.index(temp1[k]) > stand.index(temp2[k]):
                    return 1
                if stand.index(temp1[k]) < stand.index(temp2[k]):
                    return 0
        for k in range(4,-1,-1):
            if stand.index(t1[k][0]) > stand.index(t2[k][0]):
                return 1
            if stand.index(t1[k][0]) < stand.index(t2[k][0]):
                return 0

def main():
    path = 'E:\CodesPackage-notes\Python\Project-Euler\p054_poker.txt'
    file = open(path)
    mark = 0
    for each in file:
        temp = each[0:-1].split(' ')
        t1 = temp[0:5]
        t2 = temp[5:]
        if compare(t1, t2):
            mark += 1
    print(mark)
main()