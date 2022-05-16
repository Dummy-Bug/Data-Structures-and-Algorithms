"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""
# https://leetcode.com/problems/copy-list-with-random-pointer/

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        
        if not head:
            return 
        
        dx = dict()
        
        old_node = head
        
        while old_node:
            new_node   = Node(old_node.val) # creating a new node
            
            dx[old_node] = new_node # storing the key : cvalue pair in MAP
            
            old_node = old_node.next 
        
        old_node = head
        
        while old_node:
            old_node_next   = old_node.next
            old_node_random = old_node.random
            
            new_node = dx[old_node]
            
            if old_node_next == None:
                new_node_next = None
            else:
                new_node_next   = dx[old_node_next]
                
            if old_node_random == None:
                new_node_random = None
            else:
                new_node_random = dx[old_node_random]
            
            new_node.next   = new_node_next
            new_node.random = new_node_random
            
            old_node = old_node.next
        return dx[head]
            
        