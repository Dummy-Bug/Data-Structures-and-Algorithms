## Middle element of linked list

### Problem Description

Given a linked list of integers, find and return the middle element of the linked list.

**NOTE**: 

>If there are N nodes in the linked list and N is even then return the (N/2 + 1)th element

**Notes**

> Use two pointers where slow and fast by the end of the loop slow will point to the middle node of the Linekd List;

```

class Solution:

    def solve(self, head):
        slow  = head;
        fast  = head;

        while fast and fast.next:
            slow = slow.next;
            fast = fast.next.next;
        return slow.val;
        
```
