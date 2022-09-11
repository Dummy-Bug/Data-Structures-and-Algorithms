### Infix to Postfix

https://practice.geeksforgeeks.org/problems/infix-to-postfix-1587115620/1

**Notes**

-> Push the operator into stack only if stack's top element has lower priority than current element.

-> If you can come up with infix to postfix exporn in notebook then coding it ain't a hard thing.

```

from collections import deque;

class Solution:

    def solve(self, string):

        precedence = dict();

        precedence['+'] = precedence['-'] = 1;
        precedence['*'] = precedence['/'] = 2;
        precedence['^'] = 3;

        stack = deque([]);
        postfix_exprn = [];

        for char in string:

            if char not in precedence and char != ')' and char != '(':
                postfix_exprn.append(char);

            elif len(stack) == 0 or char == '(' :
                stack.append(char);
            
            elif char == ')':

                while stack[-1] != '(':
                    postfix_exprn.append(stack.pop());
                stack.pop();
            elif stack[-1] == '(' or  precedence[char] > precedence[stack[-1]]:
                stack.append(char);
            else:
                while len(stack) != 0 and stack[-1] != '(' and  precedence[char] <= precedence[stack[-1]]:
                    postfix_exprn.append(stack.pop());
                stack.append(char)
        
        while len(stack) != 0:
            postfix_exprn.append(stack.pop());

        return "".join(postfix_exprn); 

                

```
