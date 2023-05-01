### Odd and Even Levels

Problem Description
Given a binary tree of integers. Find the difference between the sum of nodes at odd level and sum of nodes at even level.

NOTE: Consider the level of root node as 1.



Problem Constraints
1 <= Number of nodes in binary tree <= 100000

0 <= node values <= 109



Input Format
First and only argument is a root node of the binary tree, A



Output Format
Return an integer denoting the difference between the sum of nodes at odd level and sum of nodes at even level.



Example Input
Input 1:

        1
      /   \
     2     3
    / \   / \
   4   5 6   7
  /
 8 
Input 2:

        1
       / \
      2   10
       \
        4


Example Output
Output 1:

 10
Output 2:

 -7


Example Explanation
Explanation 1:

 Sum of nodes at odd level = 23
 Sum of ndoes at even level = 13
Explanation 2:

 Sum of nodes at odd level = 5
 Sum of ndoes at even level = 12


```

from collections import deque;

class Solution:

    def solve(self, root):

        q = deque([root]);
        odd_sum = even_sum = level = 0;

        while q:
            curr_sum = 0;
            curr_len = len(q);

            for i in range(curr_len):

                node = q.popleft();
                curr_sum += node.val;

                if node.left:
                    q.append(node.left);
                
                if node.right:
                    q.append(node.right);
                
            if level%2 == 0:
                even_sum += curr_sum;
            else:
                odd_sum  += curr_sum;
            
            level += 1
        
        return even_sum-odd_sum;

            

```
