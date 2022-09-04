## Delete middle node of a Linked List

if given linked list is 1->2->3->4->5 then linked list should be modified to 1->2->4->5
If the input linked list has 1 node, then this node should be deleted and a null node should be returned.

**Notes**

> Use two pointers where slow and fast by the end of the loop slow will point to the middle node of the Linekd List;
> Remember Dummy Node is onluy used whene we have to return the different head or our the need of question is that our head may change;

```

class Solution:
    def solve(self, head):
        
        if head == None or head.next == None:
            return None;

        slow  = head;
        fast  = head;
        prev  = None;

        while fast and fast.next:
            prev = slow;
            slow = slow.next;
            fast = fast.next.next;
        
        prev.next = prev.next.next;
        return head;

```
