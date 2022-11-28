### Problem Description

Given the price list at which tickets for a flight were purchased, figure out the kth smallest price for the flight. kth smallest price is the 
minimum possible n such that there are at least k price elements in the price list with value <= n. In other words, if the price list was sorted, 
then A[k-1] ( k is 1 based, while the array is 0 based ).

NOTE You are not allowed to modify the price list ( The price list is read only ). Try to do it using constant extra space.

Example:

A : [2 1 4 3 2]
k : 3

Answer : 2
Constraints :

1 <= number of elements in the price list <= 1000000
1 <= k <= number of elements in the price list


```

class Solution:

    def solve(self, A, B):

        low  = 1;
        high = max(A);
        ans  = -1

        while low <= high:

            mid = (low+high)//2;

            result = self.get_smaller_elements(A,mid,B);
            
            if result == True:
                ans  = mid;
                high = mid - 1;
            else:
                low  = mid + 1;
        
        return ans;
    
    def get_smaller_elements(self,A,k,upperbound):

        start = 0;end   = len(A)-1;
        count = 0

        while start <= end:

            if A[start] <= k:
                count = count + 1;
            
            if count == upperbound:
                return True;
            
            start = start + 1;
        return False;
    

```
