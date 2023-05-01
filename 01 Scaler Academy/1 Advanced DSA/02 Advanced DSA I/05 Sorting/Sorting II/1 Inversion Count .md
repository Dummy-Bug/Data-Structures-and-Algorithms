### Problem Description

Given an array of integers A. If i < j and A[i] > A[j], then the pair (i, j) is called an inversion of A. Find the total number of 
inversions of A modulo (109 + 7).



Problem Constraints
1 <= length of the array <= 100000

1 <= A[i] <= 10^9



Input Format
The only argument given is the integer array A.



Output Format
Return the number of inversions of A modulo (109 + 7).



Example Input
Input 1:

A = [3, 2, 1]
Input 2:

A = [1, 2, 3]


Example Output
Output 1:

3
Output 2:

0


Example Explanation
Explanation 1:

 All pairs are inversions.
Explanation 2:

 No inversions.
 
 
 **Approach**
 
 Naive Approach Traverse through the array from start to end Find the count of elements smaller than the current number up to that index 
 for every element using another loop. Sum up the count of inversion for every index. Print the count of inversions.

Efficient Approach using Merge Sort

Suppose we know the number of inversions in the left half and the right half of the array, lets call them inv_l and inv_r.
Which inversions are not counted in inv_l+inv_r ? The elements in the left half which are greater than the elements in the right half. 
These are the inversions which are not counted.

Lets assume that both left half and right half are sorted. Can we count the number of inversions now?
We can just merge the two arrays and whenever we find that a[i] > a[j] (where i is the pointer of left half of the array and j is the pointer of the right half of the array) we simply increment the number of inversions.
The final answer will be inv_l + inv_r + number of inversions found during merge step.

Does this remind of a famous algorithm?

Yes, thats right. It is Merge Sort with a slight modification.
 
 ```
 
 class Solution:

    def solve(self, A):

        mod = 10**9 + 7;
        return self.merge_sort(A,0,len(A)-1,mod);
    
    def merge_sort(self,nums,low,high,mod):

        if low < high :

            middle = (low+high)//2;

            left_inversions  = self.merge_sort(nums,low,middle,mod);
            right_inversion  = self.merge_sort(nums,middle+1,high,mod);

            return (left_inversions+right_inversion+self.merge(nums,low,middle,high,mod))%mod;
        else:
            return 0;
        
    def merge(self,nums,low,middle,high,mod):

        p1 = low;       n1 = middle;
        p2 = middle+1;  n2 = high;
        
        temp = []
        inversions = 0;

        while p1<=n1 and p2<=n2:

            if nums[p1] > nums[p2]:
                inversions += (n1-p1+1);
                temp.append(nums[p2]);
                p2 = p2 + 1;
            
            else:
                temp.append(nums[p1]);
                p1 = p1 + 1;
        
        while p1<=n1:
            temp.append(nums[p1]);
            p1 += 1;
        
        while p2<=n2:
            temp.append(nums[p2]);
            p2 += 1;
        
        p3 = 0
        for i in range(low,high+1):
            nums[i] = temp[p3];
            p3 += 1;
        
        return inversions;

 
 ```
