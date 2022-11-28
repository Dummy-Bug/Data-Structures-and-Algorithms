### Reverse Nodes in group of size K

https://www.interviewbit.com/problems/k-reverse-linked-list/

### Problem Description

Given a singly linked list A and an integer B, reverse the nodes of the list B at a time and return the modified linked list.


**Notes**

> Just use link--extract--link method
> Don't use recursion as extra space is forbidden however recursive solution is very very easy to come up with;

```

class Solution:

    def reverselist(self,curr_node,count):

        prev_node = None;
        next_node = None;

        while count != 0 :
            count -= 1;
            next_node = curr_node.next;
            curr_node.next = prev_node;
            prev_node  = curr_node;
            curr_node  = next_node;
        
        return [prev_node,curr_node];

	def reverseList(self, A, B):

        # It is given that B always divides A;

        dummy = ListNode(-1);
        prev_link = dummy;

        curr = A;
        while curr:
            
            last_node = curr;
            reversed_head,next_node = self.reverselist(curr,B);
            
            prev_link.next = reversed_head;
            prev_link = last_node;
            curr = next_node;
        
        return dummy.next;
    


    

```
