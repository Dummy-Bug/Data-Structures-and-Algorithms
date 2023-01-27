### Problem Description

Given a binary tree A. Check whether it is possible to partition the tree to two trees which have equal sum of values after removing exactly one 
edge on the original tree.



Problem Constraints
1 <= size of tree <= 100000

0 <= value of node <= 109



Input Format
First and only argument is head of tree A.



Output Format
Return 1 if the tree can be partitioned into two trees of equal sum else return 0.



Example Input
Input 1:

 
                5
               /  \
              3    7
             / \  / \
            4  6  5  6
Input 2:

 
                1
               / \
              2   10
                  / \
                 20  2


Example Output
Output 1:

 1
Output 2:

 0


Example Explanation
Explanation 1:

 Remove edge between 5(root node) and 7: 
        Tree 1 =                                               Tree 2 =
                        5                                                     7
                       /                                                     / \
                      3                                                     5   6    
                     / \
                    4   6
        Sum of Tree 1 = Sum of Tree 2 = 18
Explanation 2:

The given Tree cannot be partitioned.


**Solution Approach**

After removing some edge from parent to child,
(where the child cannot be the original root)
the subtree rooted at child must be half the sum of the entire tree.

Let’s record the sum of every subtree. We can do this recursively using depth-first search.
After, we should check that half the sum of the entire tree occurs somewhere in our recording
(and not from the total of the entire tree.)


```

import sys;
sys.setrecursionlimit(10**9);

class Solution:

    def solve(self, A):
        
        self.total_sum = 0;self.ans = 0;

        self.preorder(A);
        self.helper(A);
        # print(self.total_sum);
        return self.ans;
    
    def preorder(self,node):
        if not node:
            return ;
        self.total_sum += node.val;
        self.preorder(node.left);
        self.preorder(node.right);
    

    def helper(self,node):
        if not node:
            return 0;
        left_sum  = self.helper(node.left);
        right_sum = self.helper(node.right);
        # print(left_sum,right_sum)
        if self.total_sum==2*right_sum or self.total_sum==2*left_sum:
            self.ans = 1;
            return 0;
        return left_sum+right_sum+node.val;

```
