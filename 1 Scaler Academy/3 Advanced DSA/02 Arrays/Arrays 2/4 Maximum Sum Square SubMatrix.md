### Maximum Sum Square SubMatrix

https://www.interviewbit.com/problems/maximum-sum-square-submatrix/

```

class Solution:

    def maximumSumSubarrayofsizeB(self,arr,k):
        current_sum = 0;
        n = len(arr);
        i = 0
        
        while i < k:
            current_sum += arr[i]
            i = i + 1
        max_sum = current_sum
        current_sum = current_sum - arr[0]
        
        i = 1
        while i <= (n-k):
            
            current_sum += arr[k+i-1]
            max_sum = max(current_sum,max_sum)
            current_sum  = current_sum - arr[i]
            i = i + 1
            
        return max_sum

    def solve(self, A, B):

        max_sum = float('-inf');
        N = len(A);

        for start in range(0,N-B+1):

            sum_array = [0]*B;

            end = start + B-1
            if end >= N:
                break
            summ = [0]*N

            for row in range(start,end+1):
                for col in range(N):
                    summ[col] = summ[col] + A[row][col];
            
            curr_sum = self.maximumSumSubarrayofsizeB(summ,B)
                
            max_sum  = max(curr_sum,max_sum);
        return max_sum


```



**Notes**

> Method 2- Efficient Approach:

The idea is to preprocess the given square matrix. In the preprocessing step, calculate the sum of all vertical strips of size B x 1 in a temporary square matrix stripSum[][].
Once we have the sum of all vertical strips, we can calculate the sum of the first sub-square in a row as the sum of the first B strips in that row, and for the remaining sub-squares, we can calculate the sum in O(1) time by removing the leftmost strip of the previous subsquare and adding the rightmost strip of the new square.
Time complexity of this solution is O(N2).

***Pending***


