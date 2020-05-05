# Remove Dups

def deleteDups1(n):
    _set = set()
    head = n
    prev = None
    while n != None:
        if n.val in _set:
            prev.next = n.next
        else:
            _set.add(n.val)
            prev = n
        n = n.next
    return head

# Follow Up
def deleteDups2(head):
    current = head
    while current != None:
        # Remove all future nodes that have the same value
        runner = current
        while runner.next != None:
            if runner.next.val == current.val:
                runner.next = runner.next.next
            else:
                runner = runner.next
        current = current.next
    return head

class Node(object):
    def __init__(self, data):
        self.val = data
        self.next = None
        
def display(n):
    node_list = []
    while n != None:
        node_list.append(n.val)
        n = n.next
    print(node_list)
        
def main():
    a = Node(1)
    b = Node(2) 
    c = Node(2)
    d = Node(3)
    e = Node(3)
    f = Node(3)
    g = Node(2)
    
    a.next = b
    b.next = c
    c.next = d 
    d.next = e
    e.next = f
    f.next = g
    
    display(deleteDups1(a))
    display(deleteDups2(a))
    
if __name__ == "__main__":
    main()