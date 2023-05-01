### Problem Description
Given a singly linked list A, determine if it's a palindrome. Return 1 or 0, denoting if it's a palindrome or not, respectively.

```

class Solution:
    import sys;
    sys.setrecursionlimit(10**9)
    def lPalin(self, head):
        
        slow = fast = dummy = ListNode(-1)
        dummy.next = head
        length = 0
        
        while fast and fast.next :
            
            fast = fast.next.next
            slow = slow.next

        head_B = self.reverse(slow.next)
        head_A = head
        
        while head_B :
            if head_B.val != head_A.val:
                return 0
            
            head_A = head_A.next
            head_B = head_B.next
        
        return 1
    
    def reverse(self,head):
        if head is None or head.next is None:
            return head
        
        reversed_head = self.reverse(head.next)
        
        head.next.next = head 
        head.next = None
        
        return reversed_head 

```
