### Evaluate Reverse Polish Notation

https://leetcode.com/problems/evaluate-reverse-polish-notation/

**Notes** 

--> Kinda Brute Force approach 

```
class Solution:

	def evalRPN(self, A):
		
		stack = deque();

		
		for i in range(len(A)):
			char = A[i];
			
			if char == '+':
				b = int( stack.pop() );
				a = int( stack.pop() );
				
				stack.append(str(a+b));
			
			elif char == '*':
				b = int( stack.pop() );
				a = int( stack.pop() );
				
				stack.append(str(a*b));
			
			elif char == '/':
				
				b = int( stack.pop() );
				a = int( stack.pop() );
				if (a>0 and b>0) or(a<0 and b<0):
					stack.append(str(a//b));
				else:
					stack.append(str(-1* (abs(a)//abs(b))));
			
			elif char == '-':
				b = int( stack.pop() );
				a = int( stack.pop() );
				
				stack.append(str(a-b));
			
			else:
				stack.append(char);
			
			# print(stack);
		return int(stack.pop());

```
