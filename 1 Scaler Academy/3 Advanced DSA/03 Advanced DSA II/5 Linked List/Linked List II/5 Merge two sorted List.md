### Merge Two Sorted Lists

https://www.interviewbit.com/problems/merge-two-sorted-lists/

**Notes**

* DO it just like Merge Sort with very little modification.


```

class Solution:

	def mergeTwoLists(self, A, B):

        dummy = ListNode(-1);
        ptr   = dummy;
        p1 = A; p2 = B; 

        count = 0;

        while p1 and p2:
            if p1.val < p2.val :
                ptr.next = p1;
                p1 = p1.next;
            else:
                ptr.next = p2;
                p2 = p2.next;
            
            ptr = ptr.next;
                    
        if p2:
            ptr.next = p2;
        elif p1:
            ptr.next = p1;
        return dummy.next;

```
