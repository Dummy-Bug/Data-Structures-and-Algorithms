###  Reverse Linked List

https://www.interviewbit.com/problems/reverse-linked-list/

-- Given m, n satisfy the following condition:

1 ≤ m ≤ n ≤ length of list.

---

**Notes**

> * ALways try to find the Middle of the linked list without using Recursion as there is extra space associated with recursion

> * and there are several questions that can be solved easily using non recursive reversal of linked list .

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

```
