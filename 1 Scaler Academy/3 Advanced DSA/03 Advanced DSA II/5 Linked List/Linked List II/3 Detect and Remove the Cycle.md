### Remove the loop from linked list

https://practice.geeksforgeeks.org/problems/remove-loop-in-linked-list/1

* This linked question is somewhat different

**Notes**

* We have assumed that linked list will always have cycle. But in GFG link question is slightly different.

```

class Solution:

    def solve(self, head):

        slow = head;
        fast = head;

        while fast and fast.next:
            slow = slow.next;
            fast = fast.next.next;

            if slow == fast:
                p1 = head;
                p2 = slow;
                last_node = None;

                while p1 != p2:
                    last_node = p2;
                    p1 = p1.next;
                    p2 = p2.next;
                last_node.next = None;
                return head;

```
