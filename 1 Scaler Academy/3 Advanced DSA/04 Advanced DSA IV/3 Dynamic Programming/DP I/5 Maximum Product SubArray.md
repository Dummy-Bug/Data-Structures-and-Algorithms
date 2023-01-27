### Problem Description
Given an integer array A of size N. Find the contiguous subarray within the given array (containing at least one number) which has the largest 
product.

Return an integer corresponding to the maximum product possible.

**LeetCode Solution Explanations**

-> Intution: Since we have to find the contiguous subarray having maximum product then your approach should be combination of following three cases :

Case1 :- All the elements are positive : Then your answer will be product of all the elements in the array.

Case2 :- Array have positive and negative elements both :
If the number of negative elements is even then again your answer will be complete array because on multiplying all the negative numbers it will become positive.
If the number of negative elements is odd then you have to remove just one negative element and for that u need to check your subarrays to get the max product.

Case3 :- Array also contains 0 : Then there will be not much difference...its just that your array will be divided into subarray around that 0. What u have to so is just as soon as your product becomes 0 make it 1 for the next iteration, now u will be searching new subarray and previous max will already be updated.


```

class Solution:

	def maxProduct(self, A):

        Max = Min = result = A[0];

        for i in range(1,len(A)):

            temp = Max;
            Max  = max(Max*A[i],Min*A[i],A[i]);
            Min  = min(temp*A[i],Min*A[i],A[i]);
            result = max(result,Max);
        
        return result
        
```

**Above Solution is a bit non Intiutive to come up with**

```

class Solution:
    # @param A : tuple of integers
    # @return an integer
    def maxProduct(self, A):
        n = len(A)
        # store the result that is the max we have found so far
        result = A[0]
        # Max/Min stores the max/min product of
        # subarray that ends with the current number A[i]
        Max = result
        Min = result
        for i in range(1, n):
            # multiplied by a negative makes big number smaller, small number bigger
            # so we redefine the extremums by swapping them
            if A[i] < 0:
                Max, Min = Min, Max

            # max/min product for the current number is either the current number itself
            # or the max/min by the previous number times the current one
            Max = max(A[i], Max * A[i])
            Min = min(A[i], Min * A[i])

            # the newly computed max value is a candidate for our global result
            result = max(result, Max)
        return result;


```
