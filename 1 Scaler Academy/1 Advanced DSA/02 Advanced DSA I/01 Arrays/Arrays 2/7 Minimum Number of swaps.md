### minimum Number of Swaps 

https://practice.geeksforgeeks.org/problems/minimum-swaps-required-to-bring-all-elements-less-than-or-equal-to-k-together4847/1

**Notes**

> First, we will find the number of elements that are less than or equal to B. Let the count comes out to be X.

We know that we need at most X-1 swaps to make all X elements to be consecutive.
Maintain a window of X and check how many elements we need to swap so that all X elements come in that window.

We store the minimum of all that and return that.

```

class Solution:

    def solve(self, A, B):

        total_count = 0; result = 0;
        n     = len(A);

        for i in range(n):
            if A[i] <= B:
                total_count += 1;
        
        i = j = 0;
        swaps = float('inf'); count = 0;

        while j < n:
            if j < total_count-1:
                if A[j] <= B:
                    count += 1;
                j = j + 1;
                continue
            
            if A[j] <= B:
                count += 1;
                
            swaps = min(swaps,total_count-count);

            if A[i] <= B:
                count -= 1;
            i = i + 1;
            j = j + 1;
        
        return swaps;
        

```
