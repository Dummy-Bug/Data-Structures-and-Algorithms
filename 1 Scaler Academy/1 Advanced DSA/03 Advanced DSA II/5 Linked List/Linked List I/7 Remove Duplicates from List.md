### 7 Remove Duplicates from List;

https://www.interviewbit.com/problems/remove-duplicates-from-sorted-list/

### Problem Description
Given a sorted linked list, delete all duplicates such that each element appears only once.

**Notes**
> This Variant is simple 

```

class Solution:

	def deleteDuplicates(self, A):

		curr = prev = A;

		while curr:
			if curr.val != prev.val:
				prev.next = curr;
				prev = curr;
			curr = curr.next;
		prev.next = None;
		return A;

```
