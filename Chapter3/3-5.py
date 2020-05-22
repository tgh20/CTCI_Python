# Sort Stack

class Stack(object):
    def __init__(self):
        self.stack = []
        
    def push(self, val):
        self.stack.append(val)
        
    def pop(self):
        if self.isEmpty():
            return 'Empty'
        return self.stack.pop()
    
    def peek(self):
        if self.isEmpty():
            return 'Empty'
        return self.stack[-1]
    
    def isEmpty(self):
        return len(self.stack) == 0

def SortStack(stack1):
    stack2 = Stack()
    while not stack1.isEmpty():
        tmp = stack1.pop()
        while not stack2.isEmpty() and stack2.peek() > tmp:
            stack1.push(stack2.pop())
        stack2.push(tmp)
        
    while not stack2.isEmpty():
        stack1.push(stack2.pop())
        
def main():
    arr = Stack()
    values = [1, 4, 2, 5, 6, 4, 4, 3]
    
    for i in range(len(values)):
        arr.push(values[i])
    
    SortStack(arr)
    print(arr.stack)
    
if __name__ == "__main__":
    main()