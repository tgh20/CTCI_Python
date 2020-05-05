# URLify

def replaceSpaces1(x, num):
    s = ''
    for  i in range(num):
        if x[i] == ' ':
            s += '%20'
        else:
            s += x[i]
    return s

def replaceSpaces2(x, num):
    space_count = 0
    x = list(x)
    for i in range(num):
        if x[i] == ' ':
            space_count += 1
    
    index = num + space_count * 2
    for i in range(num-1, 0, -1):
        if x[i] == ' ':
            x[index - 1] = '0'
            x[index - 2] = '2'
            x[index - 3] = '%'
            index = index - 3
        else:
            x[index - 1] = x[i]
            index -= 1
    return ''.join(x)

def main():
    string = 'Mr John Smith    '
    true_length = 13
    print(replaceSpaces1(string, true_length))
    print(replaceSpaces2(string, true_length))
    
if __name__ =="__main__":
    main()