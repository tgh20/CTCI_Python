# Delete MIddle Node

def deleteNode(n):
    if n == None or n.next == None:
        return
    
    cur = n.next
    n.val = cur.val
    n.next = cur.next
    
class Node(object):
    def __init__(self, data):
        self.val = data
        self.next = None
        
def display(node):
    node_list = []
    while node != None:
        node_list.append(node.val)
        node = node.next
    return node_list

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
    
    print("original : ", display(a))
    deleteNode(c)
    print("delete mid : ", display(a))
    
if __name__ == "__main__":
    main()