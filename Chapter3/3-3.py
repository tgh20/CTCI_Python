# Stack Of Plates

class SetOfStacks(object):
    def __init__(self, threshold):
        self.th = threshold
        self.stack = []
        
    def push(self, val):
        if len(self.stack) == 0 or len(self.stack[-1]) == self.th:
            self.stack.append([])
        self.stack[-1].append(val)
        
    def pop(self):
        if len(self.stack) == 0:
            return 'Empty Stack'
        data = self.stack[-1].pop()
        if len(self.stack[-1]) == 0:
            self.stack.pop()
        return data
    
    def popAt(self, pos):
        if len(self.stack) == 0 or len(self.stack[pos]) == 0:
            return 'Empty Stack'
        data = self.stack[pos].pop()
        return data
        
def main():
    arr = SetOfStacks(3)
    arr.push(5)
    arr.push(1)
    arr.push(2)
    arr.push(1)
    print(arr.pop())
    print(arr.popAt(0))
    print(arr.pop())

if __name__ == "__main__":
    main()