# Sum Lists

# Solution1
def addLists1(node1, node2):
    ans = []
    
    carry = 0
    while node1 !=  None and node2 != None:
        _add = node1.val + node2.val + carry
        ans.append(_add % 10)
        carry = _add // 10
        
        node1 = node1.next
        node2 = node2.next
        
    while node1 != None:
        ans.append((node1.val + carry) % 10)
        carry = (node1.val + carry) // 10
        node1 = node1.next
        
    while node2 != None:
        ans.append((node2.val + carry) % 10)
        carry = (node2.val + carry) // 10
        node2 = node2.next
        
    if carry != 0:
        ans.append(carry)
        
    ans = [str(x) for x in ans]
    return '→'.join(ans)

# Solution2
def addLists2(node1, node2, carry):
    if node1 == None and node2 == None and carry == 0:
        return None
    
    ans = Node(0)
    value = carry
    if node1 != None:
        value += node1.val
    if node2 != None:
        value += node2.val
    ans.val = value % 10
    
    # Recurse
    if node1 != None or node2 != None:
        more = addLists2(node1.next, node2.next, value//10)
        ans.next = more
    return ans

# FOLLOW UP
class PartialSum():
    _sum = None
    carry = 0
    
def addLists3(node1, node2):
    len1 = length(node1)
    len2 = length(node2)
    
    if len1 < len2:
        node1 = padList(node1, len2 - len1)
    else:
        node2 = padList(node2, len1 - len2)
    
    # Add lists
    _sum = addListsHelper(node1, node2)
    
    if _sum.carry == 0:
        return _sum._sum
    else:
        ans = insertBefore(_sum._sum, _sum.carry)
        return ans

def addListsHelper(node1, node2):
    if node1 == None and node2 == None:
        _sum = PartialSum()
        return _sum
    
    _sum = addListsHelper(node1.next, node2.next)
    value = _sum.carry + node1.val + node2.val
    full_ans = insertBefore(_sum._sum, value % 10)
    
    _sum._sum = full_ans
    _sum.carry = value // 10
    return _sum

def padList(l, padding):
    head = l
    for i in range(padding):
        head = insertBefore(head, 0)
    return head

def insertBefore(_list, data):
    node = Node(data)
    if _list != None:
        node.next = _list
    return node

def length(node):
    if node == None:
        return 0
    cnt  = 0
    while node != None:
        cnt += 1
        node = node.next
    return cnt

def display(node):
    li = []
    while node != None:
        li.append(node.val)
        node = node.next
    li = [str(x) for x in li]
    return '→'.join(li)
    
        
class Node(object):
    def __init__(self, data):
        self.val = data
        self.next = None
        
def main():
    a1 = Node(7)
    b1 = Node(1)
    c1 = Node(6)
    
    a2 = Node(5)
    b2 = Node(9)
    c2 = Node(2)
    
    a1.next = b1
    b1.next = c1
    
    a2.next = b2
    b2.next = c2
    
    A1 = Node(6)
    B1 = Node(1)
    C1 = Node(7)
    
    A2 = Node(2)
    B2 = Node(9)
#     C2 = Node(5)
    
    A1.next = B1
    B1.next = C1
    
    A2.next = B2
#     B2.next = C2
    
    print('Solution1 : ', addLists1(a1, a2))
    print('Solution2 : ', display(addLists2(a1, a2, 0)))
    print('Follow Up : ', display(addLists3(A1, A2)))
    
if __name__ == "__main__":
    main()