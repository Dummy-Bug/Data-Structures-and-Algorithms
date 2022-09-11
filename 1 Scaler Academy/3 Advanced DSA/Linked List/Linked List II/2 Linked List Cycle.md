### Detect Cycle in Linked List

https://www.interviewbit.com/problems/list-cycle/

**Notes**

* Always check for edge cases in this question

* what are possible cases for odd and even number of Nodes

* This code works only for the type of test cases mentioned in the Link

```

class Solution:

    def detectCycle(self, head):

        slow = head;
        fast = head;

        while fast and fast.next:
            slow = slow.next;
            fast = fast.next.next;

            if slow == fast:
                p1 = head;
                p2 = slow;

                while p1 != p2:
                    p1 = p1.next;
                    p2 = p2.next;
                
                return p1;
            
        return None;

```
