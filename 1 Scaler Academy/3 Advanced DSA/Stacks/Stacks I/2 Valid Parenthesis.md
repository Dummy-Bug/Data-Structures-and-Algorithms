### Check for Valid Parenthesis

https://leetcode.com/problems/valid-parentheses/

**Notes** 
-> Stack will occupy O(n) space but space used by Map is connstant.


```


from collections import deque;
class Solution:

	def solve(self, A):

        close = dict();
        close[')'] = '('; close['}'] = '{'; close[']'] = '[';

        stack = deque();

        for char in A:

            if char in close and len(stack)==0:
                return 0;
            elif char in close and stack[-1] != close[char]:
                return 0;
            elif char in close and stack[-1] == close[char]:
                stack.pop();
            else:
                stack.append(char);
        
        return 1 if  len(stack)==0 else 0;

      
```
