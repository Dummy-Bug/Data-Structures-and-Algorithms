### Problem Description

Merge two sorted linked lists, A and B, and return it as a new list.

The new list should be made by splicing together the nodes of the first two lists and should also be sorted.



Problem Constraints
0 <= |A|, |B| <= 105



Input Format
The first argument of input contains a pointer to the head of linked list A.

The second argument of input contains a pointer to the head of linked list B.



Output Format
Return a pointer to the head of the merged linked list.



Example Input
Input 1:

 A = 5 -> 8 -> 20
 B = 4 -> 11 -> 15
Input 2:

 A = 1 -> 2 -> 3
 B = Null


Example Output
Output 1:

 4 -> 5 -> 8 -> 11 -> 15 -> 20
Output 2:

 1 -> 2 -> 3


Example Explanation
Explanation 1:

 Merging A and B will result in 4 -> 5 -> 8 -> 11 -> 15 -> 20 
Explanation 2:

 We don't need to merge as B is empty. 

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
