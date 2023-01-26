### Problem Description

Given a linked list of integers. Find and return the length of the longest palindrome list that exists in that linked list.

A palindrome list is a list that reads the same backward and forward.

Expected memory complexity : O(1)



Problem Constraints
1 <= length of the linked list <= 2000

1 <= Node value <= 100



Input Format
The only argument given is head pointer of the linked list.



Output Format
Return the length of the longest palindrome list.



Example Input
Input 1:

 2 -> 3 -> 3 -> 3
Input 2:

 2 -> 1 -> 2 -> 1 ->  2 -> 2 -> 1 -> 3 -> 2 -> 2


Example Output
Output 1:

 3
Output 2:

 5


Example Explanation
Explanation 1:

 3 -> 3 -> 3 is largest palindromic sublist
Explanation 2:

 2 -> 1 -> 2 -> 1 -> 2 is largest palindromic sublist.


**Solution Approach**

N^2 solution time complexity can also pass,
So can we just retrieve the numbers from the list and them find longest
palindromic subarray??
We can iterate over the list and store all numbers
in another list. Now we can use N^2 brute force solution
to calculate the longest palindromic substring in
the given list.


```

class Solution:
    # @param A : head node of linked list
    # @return an integer
    def solve(self, A):
        dummy = ListNode(-1);cur = A
        prev  = dummy;
        ans   = 0

        while (cur != None):
            
            # Case 1: cur is a center node of palindrome of odd length
            prevItr = prev
            nextItr = cur.next
            l = 1
            while (prevItr != None and nextItr != None):
                if (prevItr.val == nextItr.val):
                    prevItr = prevItr.next
                    nextItr = nextItr.next
                    l += 1
                else: 
                    break
            ans = max(ans, l + l - 1)

            # Case 2: When palindrome length is even
            l = 0;
            prevItr = prev
            nextItr = cur
            while (prevItr != None and nextItr != None):
                if (prevItr.val == nextItr.val):
                    prevItr = prevItr.next
                    nextItr = nextItr.next
                    l += 1
                else: 
                    break
            ans = max(2 * l, ans)

            Next = cur.next
            cur.next = prev
            prev = cur
            cur = Next

        return ans


```
