# Palindrome

# Solution1 : Reverse and Compare
def isPalindrome1(head):
    _reversed = reverseAndClone(head)
    return isEqual(head, _reversed)

def reverseAndClone(node):
    head = None
    while node != None:
        n = Node(node.val) # Clone
        n.next = head
        head = n
        node = node.next
    return head

def isEqual(one, two):
    while one != None and two != None:
        if one.val != two.val:
            return False
        one = one.next
        two = two.next
    return one == None and two == None

# Solution2 : Iterative Approach
from collections import deque
def isPalindrome2(head):
    fast = head
    slow = head
    stack = deque()
    
    while fast != None and fast.next != None:
        stack.append(slow.val)
        slow = slow.next
        fast = fast.next.next
    
    # Has odd number of elements, so skip the middle element
    if fast != None:
        slow = slow.next
    
    while slow != None:
        top = stack.pop()
        if top != slow.val:
            return False
        slow = slow.next
    return True 
    
# Solution3: hash table
from collections import defaultdict
def isPalindrome3(node):
    d = defaultdict(int)
    while node != None:
        if d[node.val] == 0:
            d[node.val] = 1
        else:
            d[node.val] = 0
        node = node.next
    values = [v for k, v in d.items()]
    if sum(values) <= 1:
        return True
    return False

class Node(object):
    def __init__(self, data):
        self.val = data
        self.next = None
        
def main():
    a = Node(0)
    b = Node(1)
    c = Node(2)
    d = Node(1)
    e = Node(0)

    a.next = b
    b.next = c
    c.next = d
    d.next = e
    
    print("Solution1 : ", isPalindrome1(a))
    print("Solution2 : ", isPalindrome2(a))
    print("Solution3 : ", isPalindrome3(a))
    
if __name__ == "__main__":
    main()