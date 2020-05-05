# String Compression

# Solution1
def compress1(s):
    new_s = []
    count = 1
    for i in range(len(s)-1):
        if s[i] == s[i+1]:
            count += 1
            if i+1 == len(s)-1:
                new_s.append(s[i] + str(count))
                break
        else:
            if i+1 == len(s)-1:
                new_s.append(s[i] + str(count) + s[i+1] + '1')
                break
            new_s.append(s[i] + str(count))
            count = 1
    if len(s) <= len(new_s):
        return s
    else:
        return ''.join(new_s)
    
# Solution2
def compress2(s):
    compressed = []
    count = 0
    for i in range(len(s)):
        count += 1
        if i+1 >= len(s) or s[i] != s[i+1]:
            compressed.append(s[i])
            compressed.append(str(count))
            count = 0
    if len(s) <= len(compressed):
        return s
    else:
        return ''.join(compressed)
    
# Solution3
def compress3(s):
    final_len = countCompression(s)
    if final_len >= len(s):
        return s
    
    compressed = []
    count = 0
    for i in range(len(s)):
        count += 1
        if i+1 >= len(s) or s[i] != s[i+1]:
            compressed.append(s[i])
            compressed.append(str(count))
            count = 0
    return ''.join(compressed)

def countCompression(s):
    comp_len = 0
    for i in range(len(s)):
        if i+1 >= len(s) or s[i] != s[i+1]:
            comp_len += 2
    return comp_len

def main():
    _str = 'aabcccccaaa'
    print('# Solution1    {}   ->   {}'.format(_str, compress1(_str)))
    print('# Solution2    {}   ->   {}'.format(_str, compress2(_str)))
    print('# Solution3    {}   ->   {}'.format(_str, compress3(_str)))
    
if __name__ == "__main__":
    main()