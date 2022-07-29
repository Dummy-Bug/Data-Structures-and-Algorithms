### Problem Description

You have given a string A having Uppercase English letters.

You have to find how many times subsequence "AG" is there in the given string.

### NOTE: Return the answer modulo 109 + 7 as the answer can be very large.



### Problem Constraints

1 <= length(A) <= 105



Input Format
First and only argument is a string A.



Output Format
Return an integer denoting the answer.



### Example Input

Input 1:

 A = "ABCGAG"
Input 2:

 A = "GAB"


### Example Output

Output 1:

 3
Output 2:

 0


### Example Explanation

Explanation 1:

 Subsequence "AG" is 3 times in given string 
Explanation 2:

 There is no subsequence "AG" in the given string.
 


**Approach 1**

> Simply find the number of G’s after any index i by taking suffix sum.
Then traverse the string again, and when you encounter an ‘A’, add the number of G’s after that to the answer.

```
class Solution:
    # @param A : string
    # @return an integer
    def solve(self, A):

        n = len(A); mod = 10**9 + 7;
        suffix_arr = [0]*n;

        for i in range(n-1,-1,-1):

            if i == n-1:
                if A[i] == 'G':
                    suffix_arr[i] = 1;
                continue;
            
            if A[i] == 'G':
                suffix_arr[i] = (1 + suffix_arr[i+1])%mod;
            else:
                suffix_arr[i] = suffix_arr[i+1];

        # print(suffix_arr);
        count = 0;
        for i in range(n):

            if A[i] == 'A':
                count = (count + suffix_arr[i])%mod;
        
        return count ;
     
     
  ```
  
  
  **Approach 2**
  
  > We can Avoid the Suffix Array and take the G_count instead keep on decreasing it as we traverse the Array

```

class Solution:

    def solve(self, A):

        G_count = 0; mod = 1000000007;

        for index in range(len(A)):
        
            if A[index] == 'G':
                G_count += 1;

        subsequence_count = 0;

        for index in range(len(A)):

            if A[index] == 'A':
                subsequence_count = (subsequence_count + G_count)%mod;
            
            elif A[index] == 'G':
                G_count -= 1;

        return subsequence_count;




```

