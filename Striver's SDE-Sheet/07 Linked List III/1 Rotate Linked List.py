# https://leetcode.com/problems/rotate-list/

class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        
        # reverse the whole linked list
        # then reverse the parts separately
        
        if not head:
            return None
        ptr, length = head, 0
        
        while ptr:
            ptr  = ptr.next
            length += 1
            
        k = k%(length)
        
        if k == 0:
            return head
        
        head_of_reversed_list = self.reverse(head,length)
        
        ptr  = head_of_reversed_list
        i = 0 
        while i < k:
            ptr = ptr.next
            i = i + 1
        # ptr is pointing to the head of second part in reversed list 
        head_of_first_part    = self.reverse(head_of_reversed_list,k) # reverse the first part
        head_of_second_part   = self.reverse(ptr,length-k) # reverse the 2nd part
        head_of_reversed_list.next = head_of_second_part
        
        return head_of_first_part
        
    def reverse(self,head,n):
        
        curr = ptr = head
        prev = Next = None
        i = 0
        
        while i < n :
            Next = curr.next
            curr.next = prev
            prev, curr = curr, Next
            i = i + 1
        return prev
        
        
        