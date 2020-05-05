# Palindrome Permutation

 # Solution1
def isPalindromePermutation1(x):
    from collections import defaultdict
    x = x.replace(' ', '').lower()
    c = defaultdict(int)
    for i in x:
        c[i] += 1
    count = 0
    for j in c.values():
        if j % 2 == 1:
            count += 1
    if len(x) % 2 == 0:
        return count == 0
    else:
        return count == 1
    
# Solution2
def isPalindromePermutation2(x):
    from collections import defaultdict
    x = x.replace(' ', '').lower()
    c = defaultdict(int)
    count_odd = 0
    for i in x:
        c[i] += 1
        if c[i] % 2 == 1:
            count_odd += 1
        else:
            count_odd -= 1
    return count_odd <= 1


# Solution3
def isPalindromePermutation3(x):
    x = x.replace(' ', '').lower()
    bit_vector = createBitVector(x)
    return bit_vector == 0 or checkExactlyOneBitSet(bit_vector)

def createBitVector(x):
    bit_vector = 0
    for char in x:
        bit_vector = toggle(bit_vector, ord(char))
    return bit_vector
        
def toggle(bit_vector, index):
    if index < 0:
        return bit_vector
    mask = 1 << index
    if bit_vector & mask == 0:
        bit_vector |= mask
    else:
        bit_vector &= ~mask
    return bit_vector

def checkExactlyOneBitSet(bit_vector):
    return bit_vector & (bit_vector - 1) == 0

def main():
    s = "Tact Coa"
    print('#{}     {} : {}'.format(1, s, isPalindromePermutation1(s)))
    print('#{}     {} : {}'.format(2, s, isPalindromePermutation2(s)))
    print('#{}     {} : {}'.format(3, s, isPalindromePermutation3(s)))
    
if __name__ == "__main__":
    main()