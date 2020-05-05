# String Rotation

def isRotation(s1, s2):
    if len(s1) != len(s2):
        return False
    s1s1 = s1 + s1
    if isSubstring(s1s1, s2):
        return True
    return False
    
def isSubstring(long, short):
    if short in long:
        return True
    return False

def main():
    x = 'waterbottle'
    y = 'erbottlewat'
    print(isRotation(x, y))
    
if __name__ == "__main__":
    main()