# Three in One

class FixedMultiStack(object):
    def __init__(self, stackSize, number):
        self.stackCapacity = stackSize
        self.numberOfStacks = number
        self.values = [None] * stackSize * number
        self.sizes = [0] * number
        
        # Push value onto stack.
    def push(self, stackNum, value):
        # Check that we have space for the next element
        if self.isFull(stackNum):
            print('Full Stack')
        else:
            # Increment stack pointer and then update top value.
            self.sizes[stackNum] += 1
            self.values[self.indexOfTop(stackNum)] = value
            
    # Pop item from top stack.
    def pop(self, stackNum):
        if self.isEmpty(stackNum):
            return 'Empty Stack'
        topIndex = self.indexOfTop(stackNum)
        value = self.values[topIndex] # Get top
        self.values[topIndex] = 0 # Clear
        self.sizes[stackNum] -= 1 # Shrink
        return value
    
    # Return top element.
    def peek(self, stackNum):
        if self.isEmpty(stackNum):
            return 'Empty Stack'
        else:
            return self.values[self.indexOfTop(stackNum)]
    
    # Return if stack is empty.
    def isEmpty(self, stackNum):
        return self.sizes[stackNum] == 0
    
    # Return if stack is full.
    def isFull(self, stackNum):
        return self.sizes[stackNum] == self.stackCapacity
    
    # Return index of the top of the stack.
    def indexOfTop(self, stackNum):
        offset = stackNum * self.stackCapacity
        size = self.sizes[stackNum]
        return offset + size - 1
    
def main():
    arr = FixedMultiStack(10, 3)
    arr.push(0, 5)
    print(arr.peek(0))
    arr.push(1, 1)
    arr.push(1, 2)
    print(arr.pop(1))
    print(arr.pop(2))

if __name__ == "__main__":
    main()