### Reorder Linked List

https://www.interviewbit.com/problems/reorder-list/


**Notes**

* The question is nothing but observation 


```

class Solution:
    
    def reverseList(self, head):

        if not head or not head.next:
            return head;
        
        prev_node = None;
        curr_node = head;
        next_node = head.next;

        while curr_node:
            curr_node.next = prev_node;
            prev_node  = curr_node;
            curr_node  = next_node;
            if next_node == None:
                continue;
            next_node = next_node.next;
        
        return prev_node;

	def reorderList(self, head):

        slow = head;
        fast = head;
        prev_node =  None;

        while fast and fast.next:
            prev_node = slow;
            slow = slow.next;
            fast = fast.next.next;
        if prev_node == None:
            return head;
        prev_node.next = None;
        dummy = ListNode(-1);
        ptr   = dummy;
        
        p1 = head;
        p2 = self.reverseList(slow); 

        count = 0;

        while p1 and p2:
            if count%2 == 0:
                ptr.next = p1;
                p1 = p1.next;
            else:
                ptr.next = p2;
                p2 = p2.next;
            
            ptr = ptr.next;
            count += 1;
        
        if p2:
            ptr.next = p2;
        elif p1:
            ptr.next = p1;
        return dummy.next;

```
        


