# Next Greater Element

**Notes**

- This question is very similar to next smaller element. 

- Both these questions forms the basis of hard questions.


```

from collections import deque;

class Solution:

    def nextGreater(self, A):

        stack  = deque([]);
        result = [];

        for i in range(len(A)-1,-1,-1):
            
            while stack and stack[-1] <= A[i]:
                stack.pop();

            if not stack:
                result.append(-1);
            else:
                result.append(stack[-1]);
            stack.append(A[i]);

        return result[::-1];

```
