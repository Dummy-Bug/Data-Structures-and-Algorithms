### Problem Description
Given an array of integers A and an integer B, find and return the maximum value K such that there is no subarray in A of size K with the sum of 
elements greater than B.

**Solution Approach**

-> You need to find the maximal K.
Think of a way to do this by binary search.
You can use binary seacrh to find if a certain K is allowed or not.
if it is, you try finding a bigger answer
if not, try finding a smaller answer.

int l = 1, r = a.length;
        while(l <= r) {
            int m = (l + r) >> 1;
            if(check(a, b, m))    l = m + 1;
            else        r = m - 1;
        }
        return l-1;
How do we check for a particular K if it is allowed or not?

We can use the sliding window technique.
First we can compute the sum from 0 to k-1. Check if it is less than of equal to B or not.
To move to the next window we can simply subtract a[0] from the sum and add a[K], and repeat the process.


```

class Solution:


    def subarray_sum(self,A,k):

        curr_sum = 0 ; max_sum  = 0; 
        n = len(A)-1 ;
        i  = 0 ;j  = 0

        while j <= n :

            if j-i+1 < k:
                curr_sum = curr_sum + A[j]
                j = j + 1
                continue
        
            curr_sum = curr_sum + A[j]
            max_sum  = max(max_sum,curr_sum)
            j = j + 1;
            
            curr_sum = curr_sum - A[i]
            i = i + 1;

        return max_sum
            

    def solve(self, A, B):
    
        low  = 1;
        high = len(A);
        ans  = 0;

        while low <= high :

            mid = (low+high)//2;

            max_sum = self.subarray_sum(A,mid);

            if max_sum <= B:
                ans = mid;
                low = mid + 1;
            else:
                high = mid - 1;
                
        return ans

```
