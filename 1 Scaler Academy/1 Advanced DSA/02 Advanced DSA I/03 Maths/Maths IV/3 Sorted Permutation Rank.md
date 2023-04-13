### Problem Description

Given a string A. Find the rank of the string amongst its permutations sorted lexicographically.
Assume that no characters are repeated.

Note: The answer might not fit in an integer, so return your answer % 1000003



Problem Constraints
1 <= |A| <= 1000



Input Format
First argument is a string A.



Output Format
Return an integer denoting the rank of the given string.



Example Input
Input 1:

A = "acb"
Input 2:

A = "a"


Example Output
Output 1:

2
Output 2:

1


Example Explanation
Explanation 1:

Given A = "acb".
The order permutations with letters 'a', 'c', and 'b' : 
abc
acb
bac
bca
cab
cba
So, the rank of A is 2.
Explanation 2:

Given A = "a".
Rank is clearly 1.


**Solution Approach**

Let’s start by looking at the first character.

If the first character is X, all permutations that had the first character less than X would come before this permutation when sorted lexicographically.

The number of permutations with a character C as the first character = number of permutations possible with remaining N-1 character = (N-1)!

Then the problem reduces to finding the rank of the permutation after removing the first character from the set.

Hence,

rank = number of characters less than first character * (N-1)! + rank of permutation of the string with the first character removed
Example
Let’s say our string is “VIEW”.

Character 1: 'V'
All permutations which start with 'I', 'E' would come before 'VIEW'.
Number of such permutations = 3! * 2 = 12

Let’s now remove ‘V’ and look at the rank of the permutation ‘IEW.’

Character 2: ‘I’
All permutations which start with ‘E’ will come before ‘IEW’
Number of such permutation = 2! = 2.

Now, we will limit ourselves to the rank of ‘EW’.

Character 3:
‘EW’ is the first permutation when the 2 permutations are arranged.

So, we see that there are 12 + 2 = 14 permutations that would come before "VIEW".
Hence, the rank of permutation = 15.


```

class Solution:

	def findRank(self, A):

		n = len(A); mod = 1000003;
		result = 0;

		for i in range(n):
			count = 0;
			for j in range(i+1,n):
				if A[j]<A[i]:
					count += 1;
			result = result + ( count*self.fact(n-i-1) )%mod;
		return (result+1)%mod;

	def fact(self,num):
		if num == 0 or num == 1:
			return 1;
		return (num*self.fact(num-1))%1000003;


```

**Using In-Built Factorial**


```

from math import factorial
class Solution:
    # @param A : string
    # @return an integer
    def findRank(self, A):
        res = 0
        n = len(A)
        for i in range(n - 1):
            c = 0   # count of characters less than A[i]
            for j in range(i + 1, n):
                if A[j] < A[i]:
                    c += 1
            res += c * factorial(n - i - 1)
        return (res + 1) % 1000003
        

```
