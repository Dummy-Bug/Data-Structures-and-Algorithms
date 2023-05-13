### Problem Description 

Given the head of a singly linked list, return true if it is a 
palindrome
 or false otherwise.

 

Example 1:


Input: head = [1,2,2,1]
Output: true
Example 2:


Input: head = [1,2]
Output: false
 

Constraints:

The number of nodes in the list is in the range [1, 105].
0 <= Node.val <= 9
 

Follow up: Could you do it in O(n) time and O(1) space?

```

class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        
        slow = fast = dummy = ListNode()
        dummy.next = head
        length = 0
        
        while fast and fast.next :
            
            fast = fast.next.next
            slow = slow.next

        head_B = self.reverse(slow.next)
        head_A = head
        
        while head_B :
            if head_B.val != head_A.val:
                return False
            
            head_A = head_A.next
            head_B = head_B.next
        
        return True
    
    def reverse(self,head):
        if head is None or head.next is None:
            return head
        
        reversed_head = self.reverse(head.next)
        
        head.next.next = head 
        head.next = None
        
        return reversed_head 
  
```
