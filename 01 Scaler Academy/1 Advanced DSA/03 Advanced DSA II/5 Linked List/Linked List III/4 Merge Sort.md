### Problem Description

Sort a linked list, A in O(n log n) time using constant space complexity.


Problem Constraints
0 <= |A| = 105



Input Format
The first and the only arugment of input contains a pointer to the head of the linked list, A.



Output Format
Return a pointer to the head of the sorted linked list.



Example Input
Input 1:

A = [3, 4, 2, 8]
Input 2:

A = [1]


Example Output
Output 1:

[2, 3, 4, 8]
Output 2:

[1]


Example Explanation
Explanation 1:

 The sorted form of [3, 4, 2, 8] is [2, 3, 4, 8].
Explanation 2:

 The sorted form of [1] is [1].


**Solution Approach**

  We can try to implement either merge sort or qsort.

  Let us look at the merge sort. We start traversing the singly linked list to find the midpoint of the singly linked list.
  Now, we will sort the first half and second half separately by calling the merge sort function on them.
  Then we only have to merge the 2 lists 
  
  
  ```
  
  def merge(l1, l2):
    
    dummy = ListNode(0);
    head  = dummy

    while (l1 and l2):
        # find the smaller node
        if (l1.val <= l2.val):
            head.next = l1
            l1 = l1.next
        else:
            head.next = l2
            l2 = l2.next
        head = head.next
    # add the remaining nodes
    head.next = l1 if l1 else l2
    return dummy.next

def sortL(head):
    if (head == None or head.next == None): 
        return head
    pre, fast, slow = head, head, head
    
    # find the middle node
    while (fast and fast.next):
        pre = slow
        slow = slow.next
        fast = fast.next.next

    pre.next = None
    return merge(sortL(head), sortL(slow))
    

class Solution:

	def sortList(self, A):
	    return sortL(A)

  
  ```
