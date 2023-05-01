### Nearest Smaller element 

https://www.interviewbit.com/problems/nearest-smaller-element/

**Notes**

* Very Basic question

```

from collections import deque;

class Solution:

	def prevSmaller(self, A):

		stack = deque([]);
		result = [];

		for num in A:
			
			while stack and stack[-1] >= num:
				stack.pop();
			if not stack:
				result.append(-1);
			else:
				result.append(stack[-1]);
			stack.append(num);
		return result ;

```
