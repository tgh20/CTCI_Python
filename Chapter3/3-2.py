# Stack MIn

class StackWithMin(object):
    def __init__(self):
        self.val = []
        self.min = []
        
    def push(self, data):
        self.val.append(data)
        if  len(self.min) == 0 or self.min[-1] >= data:
            self.min.append(data)
            
    def pop(self):
        if len(self.val) == 0:
            return 'Empty Stack'
        value = self.val.pop()
        if self.min[-1] == value:
            self.min.pop()
        return value
    
    def _min(self):
        if len(self.min) == 0:
            return 'Empty'
        return self.min[-1]
    
def main():
    arr = StackWithMin()
    arr.push(5)
    arr.push(1)
    arr.push(2)
    arr.push(1)
    arr.pop()
    arr.pop()
    arr.pop()
    print(arr._min())

if __name__ == "__main__":
    main()