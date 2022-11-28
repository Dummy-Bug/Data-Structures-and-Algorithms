### Problem Description

Given a bitonic sequence A of N distinct elements, write a program to find a given element B in the bitonic sequence in O(logN) time.

NOTE:

A Bitonic Sequence is a sequence of numbers which is first strictly increasing then after a point strictly decreasing.


Problem Constraints
3 <= N <= 105

1 <= A[i], B <= 108

Given array always contain a bitonic point.

Array A always contain distinct elements.



Input Format
First argument is an integer array A denoting the bitonic sequence.

Second argument is an integer B.



Output Format
Return a single integer denoting the position (0 index based) of the element B in the array A if B doesn't exist in A return -1.



Example Input
Input 1:

 A = [3, 9, 10, 20, 17, 5, 1]
 B = 20
Input 2:

 A = [5, 6, 7, 8, 9, 10, 3, 2, 1]
 B = 30


Example Output
Output 1:

 3
Output 2:

 -1


Example Explanation
Explanation 1:

 B = 20 present in A at index 3
Explanation 2:

 B = 30 is not present in A
 
 
 **Solution Approach**
 
 A simple solution is to do linear search. Time complexity of this solution would be O(N).

An efficient solution is based on Binary Search. The idea is to find the bitonic point k which is the index of the maximum element of given sequence. If the element to be searched is greater than maximum element return -1, else search the element in both halves. Below is the step by step algorithm on how to do this.

Find the bitonic point in the given array, i.e the maximum element in the given bitonic array. This can be done in log(N) time by modifying the binary search algorithm. You can refer to this post on how to do this.
If the element to be searched is equal to the element at bitonic point then print the index of bitonic point.
If the element to be searched is greater than element at bitonic point then element does not exist in the array.
If the element to be searched is less than element at bitonic point then search for element in both half of the array using binary search.
 
 ```
 
 class Solution:

    def solve(self, A, B):
        
        low  = 0;
        high = len(A) - 1;
        index = -1;
        
        while low <= high:
            
            mid = (high+low)//2;
            
            if mid-1 >= 0 and mid+1 < len(A):
                
                if A[mid-1] < A[mid]  and A[mid] > A[mid+1]:
                    index = mid+1;
                    break;
            
            if mid+1 >= len(A):
                if A[mid] < A[mid-1]:
                    index = mid;
                    break;
            
            if A[mid] > A[mid-1]:
                low = mid + 1;
                continue;
                
            if A[mid] > A[mid+1]: 
                high = mid - 1;
        
        pos1 = self.binary_search1(A,0,index-1,B);
        
        pos2 = self.binary_search2(A,index,len(A)-1,B);
        
        if pos1 == -1:
            return pos2;
        
        return pos1;
    
    def binary_search1(self,A,low,high,target):
        
        while low<=high:
            
            mid = (low+high)//2;
            
            if A[mid] == target:
                return mid;
            
            if A[mid] <  target:
                low = mid + 1;
            
            else:
                high = mid - 1;
        return -1;
    
    def binary_search2(self,A,low,high,target):
       
        while low<=high:
            
            mid = (low+high)//2;
            
            if A[mid] == target:
                return mid;
            
            if A[mid] < target:
                high = mid - 1;
            else:
                low = mid + 1;
        
        return -1
                
 
 ```
