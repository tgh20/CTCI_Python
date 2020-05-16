# Intersection

def findIntersection(list1, list2):
    if list1 == None or list2 == None:
        return None
    
    # Get tail and sizes
    result1 = getTailAndSize(list1)
    result2 = getTailAndSize(list2)
    
    # If different tail nodes, then there's no intersection.
    if result1.tail != result2.tail:
        return None
    
    # Set pointers to the start of each linked list.
    if result1.size < result2.size:
        shorter = list1
        longer = list2
    else:
        shorter = list2
        longer = list1
    
    # Advance the pointer for the longer linked list by difference in length.
    longer = getKthNode(longer, abs(result1.size - result2.size))
    
    # Move both pointers until you have a collision.
    while shorter != longer:
        shorter = shorter.next
        longer = longer.next
        
    # Return either one.
    return longer

class Result(object):
    def __init__(self, tail, size):
        self.tail = tail
        self.size = size

def getTailAndSize(_list):
    if _list == None:
        return None
    
    size = 1
    current = _list
    while current.next != None:
        size += 1
        current = current.next
    return Result(current, size)

def getKthNode(head, k):
    current = head
    while k > 0 and current != None:
        current = current.next
        k -= 1
    return current
    
class Node(object):
    def __init__(self, data):
        self.val = data
        self.next = None
    
def main():
    a = Node(3)
    b = Node(1)
    c = Node(5)
    d = Node(9)
    e = Node(7)
    f = Node(2)
    g = Node(1)
    h = Node(4)
    i = Node(6)
    
    a.next = b
    b.next = c
    c.next = d
    d.next = e
    e.next = f
    f.next = g
    
    h.next = i
    i.next = e
    
    if findIntersection(a, h):
        print(findIntersection(a, h).val)
    else:
        print(None)
    
if __name__ == "__main__":
    main()