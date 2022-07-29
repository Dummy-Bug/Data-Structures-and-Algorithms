**Given an array Arr of length N. Determine if there exists an element in the array such that the sum of the elements on its left is equal to the sum of the elements on its right. If there are no elements to the left/right, then the sum is considered to be zero. **

https://practice.geeksforgeeks.org/problems/equal-sum0810/1 

**NOTES**

> Trivial problem but catch here is instead of using prefix and suffix sum we can do it in O(1) space

**Prefix and Suffix Sum**
``` 
class Solution:

    def equilibrium(self,A,n): 
        

        prefix_sum = [A[0]]*len(A);
        suffix_sum = [A[-1]]*len(A);

        for i in range(1,len(A)):
            lower_indices_sum     = prefix_sum[i-1] + A[i];
            prefix_sum[i] = lower_indices_sum;

        for i in range(len(A)-2,-1,-1):
            higher_indices_sum = suffix_sum[i+1] + A[i];
            suffix_sum[i] = higher_indices_sum


        for i in range(len(A)):
            if prefix_sum[i] == suffix_sum[i]:
                return "YES";
        
        return "NO"
```        

**Left and Right sum**
```
class Solution:

	def equilibrium(self,A,n): 
        

        left_sum  = 0;
        right_sum = 0;

        for i in range(len(A)):
            right_sum += A[i];
        
        for i in range(len(A)):

            left_sum += A[i];
            
            if left_sum == right_sum:
                return "YES";
                
            right_sum  -= A[i];

        return "NO";
    ```

