### Problem Description

Given a linked list where every node represents a linked list and contains two pointers of its type:

Pointer to next node in the main list (right pointer)
Pointer to a linked list where this node is head (down pointer). All linked lists are sorted.
You are asked to flatten the linked list into a single list. Use down pointer to link nodes of the flattened list. The flattened linked list should also be sorted.



Problem Constraints
1 <= Total nodes in the list <= 100000

1 <= Value of node <= 109



Input Format
The only argument given is head pointer of the doubly linked list.



Output Format
Return the head pointer of the Flattened list.



Example Input
Input 1:

   3 -> 4 -> 20 -> 20 ->30
   |    |    |     |    |
   7    11   22    20   31
   |               |    |
   7               28   39
   |               |
   8               39
Input 2:

   2 -> 4 
   |    |       
   7    11    
   |            
   7


Example Output
Output 1:

 3 -> 4 -> 7 -> 7 -> 8 -> 11 -> 20 -> 20 -> 20 -> 22 -> 28 -> 30 -> 31 -> 39 -> 39 
Output 2:

 2 -> 4 -> 7 -> 7 -> 11


Example Explanation
Explanation 1:

 The return linked list is the flatten sorted list.


**Solution Approach**

What if we were given only two lists how we would have mergerd them?

The idea is to extend the same on multiple lists, select any two list and merge them to make a single list.

Now we have (total - 1) lists to merge, again repeat the above process untill we have only one list left.

```


"""
class ListNode:
    def __init__(self,x):
        self.val=x
        self.right=None
        self.down=None
"""

def flatten(root):

    if not root or root.right == None:
        return root;
    
    curr = root;
    Next = root.right;

    while Next:

        curr = merge(curr,Next);
        Next = Next.right;
    return curr;

def merge(headA,headB):
    
    dummy = ListNode(0)
    prev  = dummy # creating a new node that will be pointing to prevNode
    
    while headA and headB:
        
        if headA.val <= headB.val:
            prev.down = headA
            prev  = headA
            headA = headA.down
        else:
            prev.down = headB
            prev  = headB
            headB = headB.down
    
    if headA:
        prev.down = headA
    if headB:
        prev.down = headB
    
    return dummy.down
    
```
