https://practice.geeksforgeeks.org/problems/max-min/1?utm_source=gfg&utm_medium=article&utm_campaign=bottom_sticky_on_article

Given an array A of size N of integers. Your task is to find the sum of minimum and maximum element in the array.

Example 1:

Input:
N = 5
A[] = {-2, 1, -4, 5, 3}
Output: 1
Explanation: min = -4, max =  5. Sum = -4 + 5 = 1
 

Example 2:

Input:
N = 4
A[]  = {1, 3, 4, 1}
Output: 5
Explanation: min = 1, max = 4. Sum = 1 + 4 = 5
 

Your Task:  
You don't need to read input or print anything. Your task is to complete the function findSum() which takes the array A[] and its size N as inputs and returns the summation of minimum and maximum element of the array.

 

Expected Time Complexity: O(N)
Expected Auxiliary Space: O(1)


**Maximum and minimum of an array by comparing in pairs**

*If n is odd then initialize min and max as the first element. 
If n is even then initialize min and max as minimum and maximum of the first two elements respectively. 
For the rest of the elements, pick them in pairs and compare their 
maximum and minimum with max and min respectively.*


```

class Solution:
    def findSum(self,A,N): 
        if N == 1:
            return 2*A[0];
        if N == 2:
            return sum(A);
        if N&1 == 0:
            minValue = min(A[0],A[1]);
            maxValue = max(A[0],A[1]);
            i = 2;
        else:
            minValue = A[0];
            maxValue = A[0];
            i = 1;

        while i < N-1:
            
            if A[i] < A[i+1]:
                minValue = min(minValue,A[i]);
                maxValue = max(maxValue,A[i+1]);
            else:
                minValue = min(minValue,A[i+1]);
                maxValue = max(maxValue,A[i]);

            i += 2;
        return minValue+maxValue;
        
```

**Time Complexity**

Time Complexity: O(n)
Auxiliary Space: O(1) as no extra space was needed.

The total number of comparisons: Different for even and odd n, see below: 

       If n is odd:    3*(n-1)/2  
       If n is even:   1 Initial comparison for initializing min and max, 
                           and 3(n-2)/2 comparisons for rest of the elements  
                      =  1 + 3*(n-2)/2 = 3n/2 -2
The second and third approaches make an equal number of comparisons when n is a power of 2. 
In general, method 3 seems to be the best.
Please write comments if you find any bug in the above programs/algorithms or a better way to solve the same problem.
