#  isUnique

# hashtable
from collections import defaultdict
def isUnique1(x):
    if len(x) > 128:
        return False
    
    c = defaultdict()
    for i in x:
        if i in c:
            return False
        c[i] = 1
    return True

# create an array of boolean values
def isUnique2(x):
    if len(x) > 128:
        return False
    char_set = [0] * 128
    for i in x:
        val = ord(i)
        if char_set[val]:  # Already found this char in string
            return False
        char_set[val] = 1
    return True

# using bit vector
def isUnique3(x):
    checker = 0
    for i in x:
        val = ord(i) - ord('a')
        if checker & (1 << val) > 0:
            return False
        checker |= (1 << val)
    return True

# without additional data structures
def isUnique4(x):
    x = sorted(x)
    for i in range(len(x)-1):
        if x[i] == x[i+1]:
            return False
    return True

def main():
    w1 = 'dog'
    w2 = 'cook'
    print('#1   {} : {},    {} : {}'.format(w1, isUnique1(w1), w2, isUnique1(w2)))
    print('#2   {} : {},    {} : {}'.format(w1, isUnique1(w1), w2, isUnique2(w2)))
    print('#3   {} : {},    {} : {}'.format(w1, isUnique1(w1), w2, isUnique3(w2)))
    print('#4   {} : {},    {} : {}'.format(w1, isUnique1(w1), w2, isUnique4(w2)))
    
if __name__ == "__main__":
    main()