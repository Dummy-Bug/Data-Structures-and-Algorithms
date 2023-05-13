### Problem Description 

Given the head of a linked list, remove the nth node from the end of the list and return its head.

 

Example 1:


Input: head = [1,2,3,4,5], n = 2
Output: [1,2,3,5]
Example 2:

Input: head = [1], n = 1
Output: []
Example 3:

Input: head = [1,2], n = 1
Output: [1]
 

Constraints:

The number of nodes in the list is sz.
1 <= sz <= 30
0 <= Node.val <= 100
1 <= n <= sz
 
 
 
 ```
 
 class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        
        fast = slow = head;
        
        for _ in range(n):
            fast = fast.next;

        prev = None;
        while fast:
            fast = fast.next;
            prev = slow;
            slow = slow.next;
        if not prev:
            return head.next;
        prev.next = prev.next.next;
        
        return head;
 
 ```
