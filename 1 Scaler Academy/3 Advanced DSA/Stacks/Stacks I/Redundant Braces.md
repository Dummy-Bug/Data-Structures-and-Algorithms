## Check if Braces are redudant or not

https://www.interviewbit.com/problems/redundant-braces/

**Notes**

* The key to solve such question is to find out what information to put inside the stack and what not..

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
