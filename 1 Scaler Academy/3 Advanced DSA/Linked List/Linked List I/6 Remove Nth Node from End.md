### Nth node from End;

https://www.interviewbit.com/problems/remove-nth-node-from-list-end/

**Notes**

> Handle the Edge Cases carefully;

```

class Solution:

    def removeNthFromEnd(self, A, B):
        
        slow = fast = A;
        
        for i in range(B+1):
            fast = fast.next;
            if not fast:
                A = A.next;
                return A
        
        while fast:
            slow = slow.next;
            fast = fast.next;
        slow.next = slow.next.next;
        
        
