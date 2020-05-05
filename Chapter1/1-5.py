# One Away

def oneEditAway1(str1, str2):
    count = 0
    pointer1 = 0
    pointer2 = 0
    if abs(len(str1) - len(str2)) > 1:
        return False
    elif len(str1) == len(str2):
        for i in range(len(str1)):
            if str1[i] != str2[i]:
                count += 1
        return count <= 1
    else:
        if len(str1) > len(str2):
            for j in range(len(str2)):
                if str1[pointer1] != str2[pointer2]:
                    count += 1
                    pointer1 += 1
                else:
                    pointer1 += 1
                    pointer2 += 1
            return count <= 1
        else:
            for k in range(len(str1)):
                if str1[pointer1] != str2[pointer2]:
                    count += 1
                    pointer2 += 1
                else:
                    pointer1 += 1
                    pointer2 += 1
            return count <= 1
        
# merge insert method and replace method
def oneEditAway2(str1, str2):
    if abs(len(str1) - len(str2)) > 1:  # length checks
        return False
    
    if len(str1) < len(str2):   # Get shorter and longer string
        s1 = str1
        s2 = str2
    else:
        s1 = str2
        s2 = str1
        
    index1 = 0
    index2 = 0
    diff = False
    while index2 < len(s2) and index1 < len(s1):
        if s1[index1] != s2[index2]:
            if diff:     # Ensure that this is the first difference found
                return False
            diff = True
            if len(s1) == len(s2):   # On replace, move shorter pointer
                index1 += 1
        else:
            index1 += 1   # If matching, move shorter pointer
        index2 += 1       # Always move pointer for longer string
    return True
    
        
def main():
    print('Solution1')
    print('{}, {}   ->   {}'.format('pale', 'ple', oneEditAway1('pale', 'ple')))
    print('{}, {}   ->   {}'.format('pales', 'pale', oneEditAway1('pales', 'pale')))
    print('{}, {}   ->   {}'.format('pale', 'bale', oneEditAway1('pale', 'bale')))
    print('{}, {}   ->   {}'.format('pale', 'bae', oneEditAway1('pale', 'bae')))
    
    print('\nSolution2')
    print('{}, {}   ->   {}'.format('pale', 'ple', oneEditAway2('pale', 'ple')))
    print('{}, {}   ->   {}'.format('pales', 'pale', oneEditAway2('pales', 'pale')))
    print('{}, {}   ->   {}'.format('pale', 'bale', oneEditAway2('pale', 'bale')))
    print('{}, {}   ->   {}'.format('pale', 'bae', oneEditAway2('pale', 'bae')))
    
if __name__ == "__main__":
    main()