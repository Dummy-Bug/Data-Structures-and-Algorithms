# https://leetcode.com/problems/reverse-linked-list/submissions/id
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        if head is None or head.next is None:
            return head
        
        reversed_head = self.reverseList(head.next)
        
        head.next.next = head # current_node is nothing but head so store it's address into next node's next
        head.next = None
        
        return reversed_head  # reversed_head contain the address of last Node which will be propgated 
                              # from last node to the very begining.
        
        
        
        