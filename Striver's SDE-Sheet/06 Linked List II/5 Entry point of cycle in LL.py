# https://leetcode.com/problems/linked-list-cycle-ii/
class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        slow = fast = head 
        
        while fast and fast.next:
            
            print(slow.val,fast.val)
            slow = slow.next
            fast = fast.next.next
            
            if slow == fast:
                break
        else: # if No cycle is present
            return None

        slow = head
        fast = fast
        
        while slow != fast:
            slow = slow.next
            fast = fast.next
        
        return slow
        