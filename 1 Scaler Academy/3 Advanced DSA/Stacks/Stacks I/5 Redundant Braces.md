## Check if Braces are redudant or not

https://www.interviewbit.com/problems/redundant-braces/

**Notes**

* The key to solve such question is to find out what information to put inside the stack and what not..

**Approach**
If we somehow pick out sub-expressions surrounded by ( and ), then if we are left with () as a part of the string, we know we have redundant braces.

Let us take an example:

(a+(a+b))

We keep pushing elements onto the stack till we encounter ')'. When we encounter ')', we start popping elements until we find a matching '('. 
If the number of elements popped does not correspond to '()', we are fine, and we can move forward. 
Otherwise, voila! Matching braces have been found. 
Some Extra Hints:

Try to run your code on test cases like (a*(a))  and (a) ??

```

class Solution:

	def braces(self, A):
        
        stack = [];
        
        for i in range(len(A)):
            
            char = A[i];
            
            if char != ")":
                stack.append(char);
                continue;
                
            symbol_count = 0;
            while stack != []:
                top = stack.pop();
                if top == '(':
                    break;
                if top == '+' or top == '-' or top == '*' or top == '/':
                    symbol_count += 1;
                    
            if symbol_count == 0:
                return 1;
        return 0;
                
                
```
