## Reverse Linked List II

### Problem Description

Reverse a linked list A from position B to C.

NOTE: Do it in-place and in one-pass.


https://www.interviewbit.com/problems/reverse-link-list-ii/ 


**NOTES**

> only two Edge cases are possible one invoving changing the head and other without changing the head.

> use link--extract--link technique 

> If you are still stuck at reversing the full linked list problem,
then would maintaining curNode, nextNode and a tmpNode help?

Maybe at every step, you do something like this :

    tmp = nextNode->next;
            nextNode->next = cur;
            cur = nextNode;
            nextNode = tmp;
Now, let’s say you did solve the problem of reversing the linked list and are stuck at applying it to the current problem.
What if your function reverses the linked list and returns the endNode of the list.
You can simply do
prevNodeOfFirstNode->next = everseLinkedList(curNode, n - m + 1);

Explanation in the video:
We can also find the two pointers between which the list needs to be reversed and only reverse that portion.
We will also have to make two new connections, one from the node just before the first node in the original portion to the node at the starting of the reversed portion, another from the first node of the original portion to the node after the last node in the original portion.

```

class Solution:

    def reverseList(self,head,count):
        
        prev_node = None;
        curr_node = head; prev_first_node = head;
        next_node = head.next;

        while count != 0 :
            count -= 1;
            next_node = curr_node.next;
            curr_node.next = prev_node;
            prev_node  = curr_node;
            curr_node  = next_node;
        
        prev_first_node.next = curr_node;
        return prev_node;

    def reverseBetween(self, A, B, C):

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


