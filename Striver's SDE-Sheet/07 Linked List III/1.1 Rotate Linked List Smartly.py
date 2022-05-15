# https://leetcode.com/problems/rotate-list/

class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        
        if not head:
            return None
        length = 1 # number of Nodes in the Linked List
        
        tail = head
        
        while tail.next :
            tail = tail.next
            length += 1
        # connect tail to the head of the linked list
        
        tail.next = head 
        
        last_node_index = length - k%(length)
        
        for i in range(0,last_node_index):
            tail = tail.next
        
        new_head  = tail.next
        tail.next = None
        
        return new_head