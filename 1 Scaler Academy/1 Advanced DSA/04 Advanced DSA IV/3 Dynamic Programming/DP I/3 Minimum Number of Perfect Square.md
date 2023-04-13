#### Problem Description

Given an integer A. Return minimum count of numbers, sum of whose squares is equal to A.



Problem Constraints
1 <= A <= 105



Input Format
First and only argument is an integer A.



Output Format
Return an integer denoting the minimum count.



Example Input
Input 1:

 A = 6
Input 2:

 A = 5


Example Output
Output 1:

 3
Output 2:

 2


Example Explanation
Explanation 1:

 Possible combinations are : (12 + 12 + 12 + 12 + 12 + 12) and (12 + 12 + 22).
 Minimum count of numbers, sum of whose squares is 6 is 3. 
Explanation 2:

 We can represent 5 using only 2 numbers i.e. 12 + 22 = 5




**Memoization**


```

import sys;
sys.setrecursionlimit(10**7);

class Solution:

	def countMinSquares(self, A):
        # greedy appproach would fail for A = 12;
        # Draw backtracking Tree and find the optimal SubProblems

        temp_arr = [-1]*(A+1); # as in worst case we will take 1^2 only;

        temp_arr[0] = 0; 

        self.helper(A,temp_arr);
        return temp_arr[A];
    
    def helper(self,num,temp_arr):

        if temp_arr[num] != -1:
            return temp_arr[num];
        
        i = 1; ans = float('inf');
        while i**2 <= num:
            ans = min(self.helper(num-i**2,temp_arr),ans);
            i  += 1;
        temp_arr[num] = ans+1;
        return temp_arr[num];


```


**Bottom Up**


```

class Solution:

	def countMinSquares(self, A):
        # greedy appproach would fail for A = 12;
        # Draw backtracking Tree and find the optimal SubProblems

        temp_arr = [-1]*(A+1); # as in worst case we will take 1^2 only;

        temp_arr[0] = 0; 

        for i in range(1,A+1):

            k = 1; ans = float('inf');
            while k**2 <= i:
                ans = min(temp_arr[i-k**2],ans);
                k  += 1;
            temp_arr[i] = ans+1;
        
        return temp_arr[A];
        

```
