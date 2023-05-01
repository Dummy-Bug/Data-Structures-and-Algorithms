
https://www.interviewbit.com/problems/assign-mice-to-holes/



**Approach 🦖**

sort mice positions (in any order)
sort hole positions 

Loop i = 1 to N:
    update ans according to the value of |mice(i) - hole(i)|

Proof of correctness:

Let i1 < i2 be the positions of two mice and let j1 < j2 be the positions of two holes.
It suffices to show via case analysis that.

max(|i1 - j1|, |i2 - j2|) <= max(|i1 - j2|, |i2 - j1|) , 
    where '|a - b|' represent absolute value of (a - b)
since it follows by induction that every assignment can be transformed by a series of swaps into the sorted assignment, where none of these swaps increases the makespan.

**Notess**
-> Proof of this question should have been asked or else question seems to be trivial

```

class Solution:

	def mice(self, A, B):

        A.sort();B.sort();

        max_time = 0;

        for i in range(len(A)):
            max_time = max(max_time,abs(A[i]-B[i]));
			
        return max_time;

```
