# https://leetcode.com/problems/linked-list-cycle/
class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
         
        # The other solution could be storing pointers in Map if duplicate appear then return true
        slow = fast = dummy = ListNode()
        dummy.next = head
        
        while fast and fast.next: # When this condition gets False it means there is No cycle
            
            fast = fast.next.next
            slow = slow.next
            
            if slow == fast:
                return True
        else:
            return False