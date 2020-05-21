# Queue via Stacks

class MyQueue(object):
    def __init__(self):
        self.stack1 = []
        self.stack2 = []
        
    def add(self, val):
        while self.stack2 != []:
            self.stack1.append(self.stack2.pop())
        self.stack1.append(val)
        
    def remove(self):
        while self.stack1 != []:
            self.stack2.append(self.stack1.pop())
        if self.stack2 == []:
            return 'Empty'
        return self.stack2.pop()
    
    def peek(self):
        while self.stack1 != []:
            self.stack2.append(self.stack1.pop())
        if self.stack2 == []:
            return 'Empty'
        return self.stack2[-1]
    
def main():
    arr = MyQueue()
    arr.add(1)
    arr.add(2)
    arr.add(3)
    print(arr.remove())
    arr.add(4)
    print(arr.remove())
    print(arr.remove())
    print(arr.peek())
    print(arr.remove())
    print(arr.remove())
    
if __name__ == "__main__":
    main()