# https://leetcode.com/problems/reverse-linked-list/
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        current = head
        prev    = None
        
        while current:
            
            Next = current.next
            current.next = prev
            prev = current
            current = Next
        
        return prev