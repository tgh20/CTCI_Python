# Partition

def partition(n, x):
    head = n
    tail = n
    while n != None:
        cur = n.next
        if n.val >= x:
            tail.next = n
            tail = tail.next
        else:
            n.next  = head
            head = n
        n = cur
    tail.next = None
    return head

def display(node):
    li = []
    while node != None:
        li.append(node.val)
        node = node.next
    return li

class Node(object):
    def __init__(self, data):
        self.val = data
        self.next = None

def main():
    a = Node(3)
    b = Node(5) 
    c = Node(8)
    d = Node(5)
    e = Node(10)
    f = Node(2)
    g = Node(1)
    
    a.next = b
    b.next = c
    c.next = d 
    d.next = e
    e.next = f
    f.next = g
    
    print(display(partition(a, 5)))
    
if __name__ == "__main__":
    main()