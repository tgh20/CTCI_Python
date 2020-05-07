# Return Kth to Last

# Solution1
def KthToLast1(node, k):
    length = getLength(node)
    num = length - k
    c = 0
    while node != None:
        if c == num:
            return node.val
        node = node.next
        c += 1
    return None
        
def getLength(n):
    head = n
    count = 0
    while head != None:
        count += 1
        head = head.next
    return count

# Solution2
def KthToLast2(head, k):
    if head == None:
        return 0
    index = KthToLast2(head.next, k) + 1
    if index == k:
        print(head.val)
    return index

# Solution3
def KthToLast3(head, k):
    p1 = head
    p2 = head
    
    # Move p1 k nodes into the list.
    for i in range(k):
        if p1 == None:
            return None   # Out of bounds
        p1 = p1.next
        
    # Move them at the same pace. When p1 hits the end, p2 will be at the right element.
    while p1 != None:
        p1 = p1.next
        p2 = p2.next
    return p2.val
    

class Node(object):
    def __init__(self, data):
        self.val = data
        self.next = None

def main():
    a = Node(1)
    b = Node(2) 
    c = Node(3)
    d = Node(4)
    e = Node(5)
    f = Node(6)
    g = Node(7)
    
    a.next = b
    b.next = c
    c.next = d 
    d.next = e
    e.next = f
    f.next = g
    
    print(KthToLast1(a, 3))
    KthToLast2(a, 3)
    print(KthToLast3(a, 3))
    
if __name__ == "__main__":
    main()