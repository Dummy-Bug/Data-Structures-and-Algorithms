### Problem Description

Given a 2 x N grid of integer, A, choose numbers such that the sum of the numbers is maximum and no two chosen numbers are adjacent horizontally, vertically or diagonally, and return it.

Note: You can choose more than 2 numbers.



Problem Constraints

1 <= N <= 20000
1 <= A[i] <= 2000



Input Format

The first and the only argument of input contains a 2d matrix, A.



Output Format

Return an integer, representing the maximum possible sum.



Example Input

Input 1:

 A = [   
        [1]
        [2]    
     ]
Input 2:

 A = [   
        [1, 2, 3, 4]
        [2, 3, 4, 5]    
     ]


Example Output

Output 1:

 2
Output 2:

 8


Example Explanation

Explanation 1:

 We will choose 2.
Explanation 2:

 We will choose 3 and 5.




**Solution Approach**


V : 
1 |  2  |  3  | 4
2 |  3  |  4  | 5

Lets first try to reduce it into a simpler problem. 
We know that within a column, we can choose at max 1 element. 
And choosing either of those elements is going to rule out choosing anything from the previous or next column. 
This means that choosing V[0][i] or V[1][i] has identical bearing on the elements which are ruled out. 
So, instead we replace each column with a single element which is the max of V[0][i], V[1][i].

Now we have the list as : 
2 3 4 5

Here we can see that we have reduced our problem into another simpler problem.
Now we want to find maximum sum of values where no 2 values are adjacent. 
Now our recurrence relation will depend only on position i and,
 a "include_current_element" which will denote whether we picked last element or not.

MAX_SUM(pos, include_current_element) = 
IF include_current_element = FALSE THEN   
    max ( MAX_SUM(pos - 1, FALSE) , MAX_SUM(pos - 1, TRUE) )

ELSE
    MAX_SUM(pos - 1, FALSE) + val(pos)
    
    
    
```
 
 
 class Solution:
    # @param A : list of list of integers
    # @return an integer
    def adjacent(self, V):
        assert(len(V) == 2 and len(V) <= 20000)
        N = len(V[0])

        MAXSUM = [[0, 0] for i in range(N+1)]
        ele = max(V[0][0], V[1][0])
        MAXSUM[0][1] = ele
        # print(MAXSUM);
        for i in range(1, N):

            # take the maximum of both the element in the current column.
            cur_element = max(V[0][i], V[1][i])

            # Case 1: Do not include current element.
            MAXSUM[i][0] = max(MAXSUM[i-1][0], MAXSUM[i-1][1])

            # Case 2: Include current element
            MAXSUM[i][1] = cur_element + MAXSUM[i-1][0]

        return max(MAXSUM[N-1][0], MAXSUM[N-1][1])
 
 
```


```

import sys;
sys.setrecursionlimit(10**9);
class Solution:

    def adjacent(self, V):

        temp = [];
        for i in range(len(V[0])):
            temp.append(max(V[0][i],V[1][i]));
        self.dp = [-1]*len(temp);
        self.dp[0] = temp[0];
        if len(temp) == 1:
            return temp[0];
            
        self.dp[1] = max(temp[0],temp[1]);
        self.helper(temp,len(temp)-1);
        return self.dp[len(temp)-1];
    
    def helper(self,arr,index):
        if self.dp[index] != -1:
            return self.dp[index];
        
        included = self.helper(arr,index-2) + arr[index] ;
        excluded = self.helper(arr,index-1);
        self.dp[index] = max(included,excluded);

        return self.dp[index];
        

```
