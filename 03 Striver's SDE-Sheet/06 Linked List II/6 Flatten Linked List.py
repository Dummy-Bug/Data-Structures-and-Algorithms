# https://practice.geeksforgeeks.org/problems/flattening-a-linked-list/1#
def flatten(root):
    
    if not root or not root.next:
        return root
    
    return helper(root)
    

def helper(headA):
    
    if headA is None or headA.next is None:
        return headA
        
    headB  = flatten(headA.next)
    
    return merge(headA,headB)

def merge(headA,headB):
    
    dummy = Node(0)
    prev  = dummy # creating a new node that will be pointing to prevNode
    
    while headA and headB:
        
        if headA.data <= headB.data:
            prev.bottom = headA
            prev  = headA
            headA = headA.bottom
        else:
            prev.bottom = headB
            prev  = headB
            headB = headB.bottom
    
    if headA:
        prev.bottom = headA
    if headB:
        prev.bottom = headB
    
    return dummy.bottom