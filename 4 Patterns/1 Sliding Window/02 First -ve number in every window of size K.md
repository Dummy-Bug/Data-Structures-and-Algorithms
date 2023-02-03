### Problem Description 

Given an array A[] of size N and a positive integer K, find the first negative integer for each and every window(contiguous subarray) of size K.


 

Example 1:

Input : 
N = 5
A[] = {-8, 2, 3, -6, 10}
K = 2
Output : 
-8 0 -6 -6
Explanation :
First negative integer for each window of size k
{-8, 2} = -8
{2, 3} = 0 (does not contain a negative integer)
{3, -6} = -6
{-6, 10} = -6
 
Example 2:
Input : 
N = 8
A[] = {12, -1, -7, 8, -15, 30, 16, 28}
K = 3
Output :
-1 -1 -7 -15 -15 0 
 

Your Task:  
You don't need to read input or print anything. Your task is to complete the function printFirstNegativeInteger() which takes the array A[], its size N and an integer K as inputs and returns the first negative number in every window of size K starting from the first till the end. If a window does not contain a negative integer , then return 0 for that window.


Expected Time Complexity: O(N)
Expected Auxiliary Space: O(K)

**Approach**

--> Problem is Variation of sliding window Maximum problem where we put inside the deque only useful elements 
    An element is useful if it is in the current window and it is a negative integer. We process all array elements one by one and maintain 
    Deque to contain useful elements of current window and these useful elements are all negative integers. For a particular window, 
    if Deque is not empty then the element at front of the Di is the first negative integer for that window, else that window does not contain 
    a negative integer.
    class Compute 
    
```
    
{

    public long[] printFirstNegativeInteger(long A[], int N, int K)
    {

        Deque<Integer> dq = new ArrayDeque<>();
        long result []    = new long [N-K+1];
        int i = 0; int j  = 0;
        
        while (j<A.length)
        {
            if ( j-i+1 < K )
            {
                if (A[j] < 0 )
                {
                    dq.add(j);
                }
                j += 1;
            }
            else
            {
                if ( A[j] < 0 )
                {
                    dq.add(j);
                }
                if (dq.size()==0)
                {
                    result[i] = 0;
                }    
                else
                {
                    result[i] = A[dq.peek()];
                }
                
                if (!dq.isEmpty() && i == dq.peek())
                    {
                        dq.remove();
                    }
                i += 1;
                j += 1;
            }
        }
        return result;
    }
}


```
