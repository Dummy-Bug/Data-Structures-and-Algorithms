### Problem Description

Given an array A of N integers.

Find the largest continuous sequence in a array which sums to zero.



Problem Constraints
1 <= N <= 106

-107 <= A[i] <= 107



Input Format
Single argument which is an integer array A.



Output Format
Return an array denoting the longest continuous sequence with total sum of zero.

NOTE : If there are multiple correct answers, return the sequence which occurs first in the array.



Example Input
A = [1,2,-2,4,-4]


Example Output
[2,-2,4,-4]


Example Explanation
[2,-2,4,-4] is the longest sequence with total sum of zero.

**Approach**

Approach:

There are two steps:

Create cumulative sum array where ith index in this array represents total sum from 1 to ith index element.
Iterate all elements of cumulative sum array and use hashing to find two elements where value at ith index == value at jth index but i != j.
IF element is not present in hash in fill hash table with current element.


```


public class Solution 
{
    public int[] lszero(int[] A) 
    {
        HashMap<Long,Integer> Hash_map = new HashMap<>();
        
        long sum = 0;
        int start_index = -1; int end_index   = -1;
        int max_length  = 0;
        Hash_map.put((long)0,-1);

        for(int i = 0; i < A.length; i++)
        {
            
            sum += A[i];

            if ( Hash_map.containsKey(sum) )
            {
                if ( max_length < (i - Hash_map.get(sum) + 1) )
                {
                start_index = Hash_map.get(sum)+1;
                end_index   = i;
                max_length  = i-Hash_map.get(sum)+1;
                }
            }
            else
            {
                Hash_map.put(sum,i);
            }
        }
        int [] result = new int[max_length-1];

        for(int i = 0; i<result.length;i++)
        {
            result[i] = A[start_index+i];
        }
        return result;
    }
}

```
