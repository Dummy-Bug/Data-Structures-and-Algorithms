# https://leetcode.com/problems/copy-list-with-random-pointer/

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        
        if not head:
            return None
        
        old_node = head
        
        while old_node: # insert the newNodes in between the oldNodes
            
            new_node = Node(old_node.val)

            new_node.next = old_node.next
            old_node.next = new_node
            
            old_node = new_node.next
        
        old_node = head 
        
        while old_node: # Insert the clone pointers
            
            new_node = old_node.next # get access to new node by going inside the next of old node.
            
            if old_node.random:
                new_node.random = old_node.random.next
            else:
                new_node.random = None
            
            old_node = new_node.next # get access to next old_node
        
        # now that we have val and random pointers it's time to separate the lists
        
        old_node  = head
        new_head = old_node.next
        
        while old_node:
            
            new_node = old_node.next
            old_node.next = new_node.next
            
            if new_node.next:
                new_node.next = new_node.next.next
            else:
                new_node.next = None
            
            old_node = old_node.next
        
        return new_head
        
            
            
        