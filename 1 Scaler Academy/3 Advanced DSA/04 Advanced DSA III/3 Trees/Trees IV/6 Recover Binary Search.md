### Problem Description

Two elements of a binary search tree (BST), represented by root A are swapped by mistake. Tell us the 2 values swapping which the tree will be 
restored.

A solution using O(n) space is pretty straightforward. Could you devise a constant space solution?



Problem Constraints
1 <= size of tree <= 100000



Input Format
First and only argument is the head of the tree,A



Output Format
Return the 2 elements which need to be swapped.



Example Input
Input 1:

 
         1
        / \
       2   3
Input 2:

 
         2
        / \
       3   1



Example Output
Output 1:

 [2, 1]
Output 2:

 [3, 1]


Example Explanation
Explanation 1:

Swapping 1 and 2 will change the BST to be 
         2
        / \
       1   3
which is a valid BST 
Explanation 2:

Swapping 1 and 3 will change the BST to be 
         2
        / \
       1   3
which is a valid BST 


**Solution Approach**

Let’s look at the inorder traversal of the tree.
In the ideal case, the inorder traversal should be sorted. But in this case, because of the swapping 2 cases might arise :
1) A sequence like {1, 4, 3, 7, 9}, where the swapped pair are adjacent to each other. Only one inversion ( Inversion here means pair of integer A[i], A[i+1] where A[i] > A[i+1] ).
2) A sequence like {1, 9, 4, 5, 3, 10} where the swapped pair are not adjacent. 2 inversions. We take the min and max of the inversion numbers, and we know the number we need to swap to get the right answer.

Now to figure this out, we need to do an inorder traversal. However, the traditional recursive inorder traversal has memory overhead of the depth of the tree.
Using a stack has the same memory overhead.

So, we need something which does not use recursion or stack and can still do the inorder traversal. This part is a bit tricky. Not all interviewers expect you to know this.
Morris traversal helps us achieve what we are after. It works on the fact that we can modify the tree when traversing and then resetting the tree to its original state once we are done.

The idea of Morris traversal is based on the Threaded Binary tree ( http://en.wikipedia.org/wiki/Threaded_binary_tree ).

In this traversal, we first create links to Inorder successor and print the data using these links, and finally revert the changes to restore the original tree.

Initialize current as root
While current is not NULL
If the current does not have left child
a) Print current’s data
b) Go to the right, i.e., current = current->right
Else
a) Make current as the right child of the rightmost node in current’s left subtree
b) Go to this left child, i.e., current = current->left
Although the tree is modified through the traversal, it is reverted back to its original shape after the completion.


```

class Solution:

	def recoverTree(self, A):

        self.prev = self.first = self.second = None;
        self.helper(A);
        return sorted([self.first.val,self.second.val])
    
    def helper(self,curr):

        if not curr:
            return;
        
        self.helper(curr.left);
        if  self.prev != None and self.prev.val > curr.val:
            if self.first == None:
                self.first = self.prev;
            self.second = curr;
        self.prev = curr;

        self.helper(curr.right);

```
