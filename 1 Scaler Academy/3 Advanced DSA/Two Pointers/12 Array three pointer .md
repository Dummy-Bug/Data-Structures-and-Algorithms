### Problem Description

You are given 3 sorted arrays A, B and C.

Find i, j, k such that : max(abs(A[i] - B[j]), abs(B[j] - C[k]), abs(C[k] - A[i])) is minimized.

Return the minimum max(abs(A[i] - B[j]), abs(B[j] - C[k]), abs(C[k] - A[i])).



Problem Constraints
0 <= len(A), len(B), len(c) <= 106

0 <= A[i], B[i], C[i] <= 107



Input Format
First argument is an integer array A.

Second argument is an integer array B.

Third argument is an integer array C.



Output Format
Return an single integer denoting the minimum max(abs(A[i] - B[j]), abs(B[j] - C[k]), abs(C[k] - A[i])).



Example Input
Input 1:

 A = [1, 4, 10]
 B = [2, 15, 20]
 C = [10, 12]
Input 2:

 A = [3, 5, 6]
 B = [2]
 C = [3, 4]


Example Output
Output 1:

 5
Output 2:

 1


Example Explanation
Explanation 1:

 With 10 from A, 15 from B and 10 from C.
Explanation 2:

 With 3 from A, 2 from B and 3 from C.
 
 
 **Approach**
 
 Windowing strategy works here.
Lets say the arrays are A,B and C.

Take 3 pointers X, Y and Z
Initialize them to point to the start of arrays A, B and C
Find min of X, Y and Z.
Compute max(X, Y, Z) - min(X, Y, Z).
If new result is less than current result, change it to the new result.
Increment the pointer of the array which contains the minimum.
Note that we increment the pointer of the array which has the minimum, because our goal is to decrease the difference. 
Increasing the maximum pointer is definitely going to increase the difference. Increase the second maximum pointer can potentially 
increase the difference ( however, it certainly will not decrease the difference ).


```

class Solution:
	# @param A : tuple of integers
	# @param B : tuple of integers
	# @param C : tuple of integers
	# @return an integer
	def minimize(self, A, B, C):
		
		p1 = p2 = p3 = 0;
		min_of_max = float('inf');
	
		
		while p1 <= len(A)-1 and p2 <= len(B)-1 and p3 <= len(C)-1:
			
			a = abs( A[p1] - B[p2] );
			b = abs( B[p2] - C[p3] );
			c = abs( C[p3] - A[p1] );
			
			max_value = max(a,b,c);
			
			min_of_max = min(max_value,min_of_max);
			
			# print(A[p1],B[p2],C[p3]);
			
			if B[p2] >= A[p1] and A[p1] <= C[p3]:
				p1 += 1;
			
			elif A[p1] >= B[p2] and B[p2] <= C[p3]:
				p2 += 1;
			else:
				p3 += 1;
			# print(p1,p2,p3,"\n");
		return min_of_max;
			
			

```
