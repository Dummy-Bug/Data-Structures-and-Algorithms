### Problem Description

Given an integer array A of size N. You have to delete one element such that the GCD(Greatest common divisor) of the remaining array is maximum.

Find the maximum value of GCD.

Example Input

Input 1:

 A = [12, 15, 18]
Input 2:

 A = [5, 15, 30]


Example Output

Output 1:

 6
Output 2:

 15


Example Explanation

Explanation 1:

 
 If you delete 12, gcd will be 3.
 If you delete 15, gcd will be 6.
 If you delete 18, gcd will 3.
 Maximum vallue of gcd is 6.
Explanation 2:

 If you delete 5, gcd will be 15.
 If you delete 15, gcd will be 5.
 If you delete 30, gcd will be 5.
 
 
 **Solution Approach**
 
We can maintain two arrays for prefix and suffix gcd; likewise, we do for prefix sum and suffix sum.
Then,for each index, i:1 to N calculate gcd(prefix[i-1],suffix[i+1]) and return the maximum among all
 
 ```
 
 class Solution:

    def solve(self, A):
        
        prefix_arr = [A[0]];
        suffix_arr = [0]*len(A);
        suffix_arr[-1] = A[-1];

        for i in range(1,len(A)):
            curr_gcd = self.gcd(A[i],prefix_arr[i-1]);
            prefix_arr.append(curr_gcd);
        
        for i in range(len(A)-2,-1,-1):
            curr_gcd = self.gcd(A[i],suffix_arr[i+1]);
            suffix_arr[i] = curr_gcd;
        
        # print(prefix_arr,suffix_arr);

        max_gcd = 1;

        for i in range(len(A)):
            
            if i == 0:
                max_gcd = max(max_gcd,suffix_arr[i+1]);
                continue;
            
            if i == len(A)-1:
                max_gcd = max(max_gcd,prefix_arr[i-1]);
                continue;
            
            curr_gcd = self.gcd(prefix_arr[i-1],suffix_arr[i+1]);
            max_gcd  = max(max_gcd,curr_gcd);
        
        return max_gcd;
    


    def gcd(self, A, B):

        if B == 0:
            return A;
        
        return self.gcd(B,A%B);

```
