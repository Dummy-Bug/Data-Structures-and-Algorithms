# https://leetcode.com/problems/remove-nth-node-from-end-of-list/
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        
        # Maintain two pointers such that the gap between them is n 
        
        if not head:
            return
        
        fast = late = dummy = ListNode()
        dummy.next = head
        for _ in range(n):
            fast = fast.next
        
        
        while fast and fast.next :
            fast = fast.next
            late = late.next
        
        late.next = late.next.next
        return dummy.next
        