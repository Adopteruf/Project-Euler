import math

def sort_in_alphabetical_order(text):
    max_num = max([len(k) for k in text])
    length = 2*(max_num - 1)
    value = []
    # encode the string to value
    for x in text:
        value.append(sum([(ord(x[y]) - ord('A') + 1)*(10**(length - 2*y)) for y in range(0, len(x))]))
    # sort the value in order
    value.sort()
    s = []
    # decode the value to string
    for k in range(0, len(value)):
        x = value[k]
        t = ''
        for j in range(length, length - 2*(max_num - 1) - 1, -2):
            if x == 0:
                break
            temp = math.floor(x / (10**j))
            t += chr(temp + ord('A') - 1)
            x -= temp*(10**j)
        s.append(t)
    return s

def get_scores(name):
    scores = 0
    for k in range(0, len(name)):
        scores += (k + 1)*sum([ord(x) - ord('A') + 1 for x in name[k]])
    return scores


file = open('E:\CodesPackage-notes\Python\Project-Euler\q22_names.txt')
text = file.read()
file.close()
text = [k[1:-1]for k in text.split(',')]

# way in mine
s1 = sort_in_alphabetical_order(text)
# way in standard lib
s2 = sorted(text)
print(get_scores(s1))
print(get_scores(s2))