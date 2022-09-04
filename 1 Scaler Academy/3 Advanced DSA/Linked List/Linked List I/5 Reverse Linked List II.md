## Reverse Linked List II

### Problem Description

Reverse a linked list A from position B to C.

NOTE: Do it in-place and in one-pass.


https://www.interviewbit.com/problems/reverse-link-list-ii/ 


**NOTES**

> only two Edge cases are possible one invoving changing the head and other without changing the head.

> use link--extract--link technique 

```

class Solution:

    def reverseList(self,head,count):
        
        prev_node = None;
        curr_node = head; prev_first_node = head;
        next_node = head.next;

        while count != 0 :
            count -= 1;
            curr_node.next = prev_node;
            prev_node  = curr_node;
            curr_node  = next_node;
            if next_node == None:
                continue;
            next_node = next_node.next;
        
        prev_first_node.next = curr_node;
        return prev_node;

    def reverseBetween(self, A, B, C):

        # reach the first node ;

        start_ptr = A; prev_node = None;

        for i in range(B-1):
            prev_node = start_ptr;
            start_ptr = start_ptr.next;
        
        if start_ptr == A: # just return new head ;
            new_head = self.reverseList(A,C-B+1);
            return new_head;
        
        else: # link the revesed node's head to the prev;
            
            prev_node.next = self.reverseList(start_ptr,C-B+1);
            return A;
        
```


