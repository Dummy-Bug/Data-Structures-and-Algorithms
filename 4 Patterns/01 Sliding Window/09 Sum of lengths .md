### Problem Description 

Given an array. Calculate the sum of lengths of contiguous subarrays having all distinct elements.

https://practice.geeksforgeeks.org/problems/sum-of-length3345/1?utm_source=gfg&utm_medium=article&utm_campaign=bottom_sticky_on_article

Example 1:

Input:
N=3
arr[] = { 1,2,3 }
Output: 10
Explanation: 
{1, 2, 3} is a subarray of length 3 with 
distinct elements. Total length of length
three = 3. {1, 2}, {2, 3} are 2 subarray 
of length 2 with distinct elements. Total 
length of lengths two = 2 + 2 = 4
{1}, {2}, {3} are 3 subarrays of length 1
with distinct element. Total lengths of 
length one = 1 + 1 + 1 = 3
Sum of lengths = 3 + 4 + 3 = 10
Example 2:

Input:
N=1
arr[] = { 1 }
Output: 1
Explanation: 
{1} is the only subarray with distinct 
elements of length 1.  

Your Task:
You don't need to read input or print anything. Your task is to complete the function sumoflength() that takes array arr and integer N as 
input parameters and returns the sum of lengths of contiguous subarrays having all distinct elements.

Expected Time Complexity: O(N).
Expected Auxiliary Space: O(N).

 

Constraints:
1 ≤ N ≤ 106


**Approach**

An efficient solution is based on the fact that if we know all elements in a subarray arr[i..j] are distinct, 
sum of all lengths of distinct element subarrays in this subarray is ((j-i+1)*(j-i+2))/2. 
Since, the possible lengths of subarrays are 1, 2, 3,……, j – i +1. So, the sum will be ((j – i +1)*(j – i +2))/2.


```

class Solution 
{
    
    long sumoflength(long arr[], int n) 
    {
        long result = 0; 
        HashSet<Long>set = new HashSet<Long>();
        
        int i = 0; int j = 0;
        
        while (i<arr.length)
        {
            while( (j<arr.length)&&(!set.contains(arr[j]) ) )
            {
                set.add(arr[j]);
                j += 1;
            }
            result = result + ( (j-i)*(j-i+1) )/2;
            set.remove(arr[i]);
            i += 1;
            
        }
        return result;
    }
}

```
