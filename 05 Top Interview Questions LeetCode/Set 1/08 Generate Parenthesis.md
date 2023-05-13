https://leetcode.com/problems/generate-parentheses/description/

### Problem Description

Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.

 

Example 1:

Input: n = 3
Output: ["((()))","(()())","(())()","()(())","()()()"]
Example 2:

Input: n = 1
Output: ["()"]
 
 
 **Approach-1**

To generate all sequences, we use a recursion. All sequences of length n is just '(' plus all sequences of length n-1, and then ')' plus all sequences of length n-1.

To check whether a sequence is valid, we keep track of balance, the net number of opening brackets minus closing brackets. If it falls below zero at any time, or doesn't end in zero, the sequence is invalid - otherwise it is valid.
 
 ```
 
 class Solution(object):
    def generateParenthesis(self, n):
        def generate(A = []):
            if len(A) == 2*n:
                if valid(A):
                    ans.append("".join(A))
            else:
                A.append('(')
                generate(A)
                A.pop()
                A.append(')')
                generate(A)
                A.pop()

        def valid(A):
            bal = 0
            for c in A:
                if c == '(': bal += 1
                else: bal -= 1
                if bal < 0: return False
            return bal == 0

        ans = []
        generate()
        return ans
 
 ```
 
**Approach-2**


```

class Solution:
    def generateParenthesis(self, n: int) -> List[str]:

        self.result = [];
        self.helper([],n,0,0);
        return self.result;
    
    def helper(self,curr_string,n,left,right):

        if len(curr_string) == 2*n:
            self.result.append("".join(curr_string));
            return
        
        if left < n:
            curr_string.append("(");
            self.helper(curr_string,n,left+1,right);
            curr_string.pop();
        if right < left:
            curr_string.append(")");
            self.helper(curr_string,n,left,right+1);
            curr_string.pop();

     

```
