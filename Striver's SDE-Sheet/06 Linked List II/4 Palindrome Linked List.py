# https://leetcode.com/problems/palindrome-linked-list/
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
            
        
        
        