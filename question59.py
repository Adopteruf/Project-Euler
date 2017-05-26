# remove some non-English written words-case to locate the possible case
#  consider 'the' to be the must frequent word
import math
from itertools import permutations

d2b = lambda x: int(str(bin(x))[2:])
b2d = lambda x: int(str(x), 2)
chract = [chr(k) for k in range(ord('a'), ord('z') + 1)]
CHRACT= [k.upper() for k in chract]
elements = chract*3
test_elements = chract + CHRACT + [' ',',','.',':',';','!','(',')','\'','\"','\n','\\']
def isdigit(n):
    try:
        num = int(n)
        return True
    except ValueError:
        return False

def xor(x, y):
    x_bin = str(d2b(x))
    y_bin = str(d2b(y))
    d = int(math.fabs((len(x_bin) - len(y_bin))))
    if len(x_bin) >= len(y_bin):
        y_bin = '0'*d + y_bin
    else:
        x_bin = '0'*d + x_bin
    b = int(''.join([str(int(x_bin[k] != y_bin[k])) for k in range(0, len(x_bin))]))
    d = int(str(b), 2)
    return d

def decode(key, data):
    keys = key*(int(len(data)/3) + 1)
    result = ''
    value = 0
    for id, each in enumerate(data):
        temp = chr(xor(int(each), ord(keys[id])))
        if test_elements.count(temp) == 0 and not isdigit(temp):
            # test it for incorrect case
            return -1, None
        value += ord(temp)
        result += temp
    if result.upper().count('the'):
        return -1, None
    return result.count('the'), value

def main():
    per_arr = permutations(elements, 3)
    per_arr = set([k[0] + k[1] + k[2] for k in per_arr])
    file = open('E:\CodesPackage-notes\Python\Project-Euler\p059_cipher.txt')
    text = file.read()
    crude_data = text[:-1].split(',')
    num_the = 0
    possible_key = 'nothing there'
    possible_value = 0
    for key in per_arr:
        temp,value = decode(key, crude_data)
        if temp > num_the:
            num_the = temp
            possible_key = key
            possible_value = value
    print(possible_key)
    print(possible_value)
main()