### Problem Description

Given an array of integers A, we call (i, j) an important reverse pair if i < j and A[i] > 2*A[j].
Return the number of important reverse pairs in the given array A.



Problem Constraints
1 <= length of the array <= 105

-2 * 109 <= A[i] <= 2 * 109



Input Format
The only argument given is the integer array A.



Output Format
Return the number of important reverse pairs in the given array A.



Example Input
Input 1:

 A = [1, 3, 2, 3, 1]
Input 2:

 A = [4, 1, 2]


Example Output
Output 1:

 2
Output 2:

 1


Example Explanation
Explanation 1:

 There are two pairs which are important reverse i.e (3, 1) and (3, 1).
Explanation 2:

 There is only one pair i.e (4, 1).


**Approach**

We can use two loops and calculate the number of pairs that satisfy the condition, but the time complexity will be O(N^2), 
which will not work in the worst case.

So we can think of a better solution, i.e., using merge sort.
We will do a usual merge sort, but before calling the merge function, we will calculate the number of pairs using two pointers, 
considering that the two arrays are sorted individually.

Likewise, we will do this till our mergesort ends, i.e., the array becomes sorted.
```

class Solution:

    def solve(self, A):

        mod = 10**9 + 7;
        return self.merge_sort(A,0,len(A)-1,mod);
    
    def merge_sort(self,nums,low,high,mod):

        if low < high :

            middle = (low+high)//2;

            left_reverse_pairs  = self.merge_sort(nums,low,middle,mod);
            right_inversion     = self.merge_sort(nums,middle+1,high,mod);

            return (left_reverse_pairs+right_inversion+self.merge(nums,low,middle,high,mod))%mod;
        else:
            return 0;
        
    def merge(self,nums,low,middle,high,mod):

        p1 = low;       n1 = middle;
        p2 = middle+1;  n2 = high;
        reverse_pairs = 0;

        while p1<=n1 and p2<=n2:

            if nums[p1] > 2*nums[p2]:
                reverse_pairs += (n1-p1+1);
                p2 = p2 + 1
            else:
                p1 += 1;
  
        p1 = low;       n1 = middle;
        p2 = middle+1;  n2 = high;
        temp = [];

        while ( p1<=n1 and p2<=n2 ):
            
            if nums[p1] > nums[p2]:
                
                temp.append(nums[p2]);
                p2 += 1;
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
        
        return reverse_pairs;

```
