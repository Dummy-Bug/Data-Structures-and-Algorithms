### Problem Description

Given an unsorted integer array A of size N.

Find the length of the longest set of consecutive elements from array A.



Problem Constraints
1 <= N <= 106

-106 <= A[i] <= 106



Input Format
First argument is an integer array A of size N.



Output Format
Return an integer denoting the length of the longest set of consecutive elements from the array A.



Example Input
Input 1:

A = [100, 4, 200, 1, 3, 2]
Input 2:

A = [2, 1]


Example Output
Output 1:

 4
Output 2:

 2


Example Explanation
Explanation 1:

 The set of consecutive elements will be [1, 2, 3, 4].
Explanation 2:

 The set of consecutive elements will be [1, 2].
 
 **Approach**
 
 One solution is to sort the elements and then find the longest subarray with consecutive elements. But this will take O(NlogN).

An efficient way is to use hashing.

First, create an empty hash, and for each element, we insert and update the hash table and maxCount.

We only insert the element which is not yet inserted.
Calculate the lcount, i.e., the longest consecutive element till the current element - 1.
Calculate the rcount, i.e., the longest consecutive element from the current element + 1.

Update hMap[ele] (current element) = lcount + 1 + rcount.

Also, update the maxCount.

 
 ```
 
 public class Solution {
    // DO NOT MODIFY THE ARGUMENTS WITH "final" PREFIX. IT IS READ ONLY
    public int longestConsecutive(final int[] A) {

        HashSet<Integer> Hash_set = new HashSet<>();
        int longest_chain = 0;


        for(int i = 0; i<A.length;i++){
            if (!Hash_set.contains(A[i])){
                Hash_set.add(A[i]);
            }
        }
        for(int i = 0;i<A.length;i++){
            
            if   ( !Hash_set.contains(A[i]-1) )
            {
                int count = 0;
                int element = A[i];
                while (Hash_set.contains(element))
                {
                    // System.out.print(element+" ");
                    count += 1;
                    element +=1;
                }
                longest_chain = Math.max(longest_chain, count);
                // System.out.print("\nchain "+longest_chain+"\n");

            }
        }
        // System.out.print(Hash_set);
        return longest_chain;
    }
}

 
 ```
