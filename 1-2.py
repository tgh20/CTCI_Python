# Check Permutation

# hashtable
from collections import defaultdict
def isPermutation1(x, y):
    c1 = defaultdict(int)
    c2 = defaultdict(int)
    if len(x) != len(y):
        return False
    for i in range(len(x)):
        c1[x[i]] += 1
        c2[y[i]] += 1
    return c1 == c2

# sort the string
def isPermutation2(x, y):
    if len(x) != len(y):
        return False
    return sorted(x) == sorted(y)

#  Check if the two string have identical character counts.
def isPermutation3(x, y):
    if len(x) != len(y):
        return False
    letters = [0] * 128  # ASCII
    for i in x:
        letters[ord(i)] += 1
    for j in y:
        letters[ord(j)] -= 1
        if letters[ord(j)] < 0:
            return False
    return True

def main():
    s1 = 'god'
    s2 = 'dog'
    print('#1  {}, {} : {}'.format(s1, s2, isPermutation1(s1, s2)))
    print('#2  {}, {} : {}'.format(s1, s2, isPermutation2(s1, s2)))
    print('#3  {}, {} : {}'.format(s1, s2, isPermutation3(s1, s2)))
    
if __name__ == "__main__":
    main()