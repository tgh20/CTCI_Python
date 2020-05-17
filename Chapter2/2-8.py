# Loop detection

def FindBeginning(head):
    slow = head
    fast = head
    
    while fast != None and fast.next != None:
        slow = slow.next
        fast = fast.next.next
        if slow == fast:
            break
        
    if fast == None or fast.next == None:
        return None
    
    fast = head
    while fast != slow:
        fast = fast.next
        slow = slow.next
        
    return fast.val

class Node(object):
    def __init__(self, data):
        self.val = data
        self.next = None
        
def main():
    a = Node('a')
    b = Node('b')
    c = Node('c')
    d = Node('d')
    e = Node('e')
    
    a.next = b
    b.next = c
    c.next = d
    d.next = e
    e.next = c
    
    print(FindBeginning(a))
    
if __name__ == "__main__":
    main()