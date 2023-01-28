### Problem Description

You are given an array A containing N numbers. This array is called special if it satisfies one of the following properties:

There exists an element A[i] in the array such that A[i] is equal to the median of elements [A[0], A[1], ...., A[i-1]]
There exists an element A[i] in the array such that A[i] is equal to the median of elements [A[i+1], A[i+2], ...., A[N-1]]
The Median is the middle element in the sorted list of elements. If the number of elements is even then the median will be 
(sum of both middle elements) / 2.

Return 1 if the array is special else return 0.

NOTE:

Do not neglect decimal point while calculating the median
For A[0] consider only the median of elements [A[1], A[2], ..., A[N-1]] (as there are no elements to the left of it)
For A[N-1] consider only the median of elements [A[0], A[1], ...., A[N-2]]


Problem Constraints
1 <= N <= 1000000.
A[i] is in the range of a signed 32-bit integer.



Input Format
The first and only argument is an integer array A.



Output Format
Return 1 if the given array is special else return 0.



Example Input
Input 1:

 A = [4, 6, 8, 4]
Input 2:

 A = [2, 7, 3, 1]


Example Output
Output 1:

 1
Output 2:

 0


Example Explanation
Explantion 1:

 Here, 6 is equal to the median of [8, 4].
Explanation 2:

 No element satisfies any condition.
 
 **Approach**
 
 This problem is the same as finding the median in a stream of numbers. You can use max and min heaps to solve this problem. 
 Following is the detailed algorithm:

Use two heaps:

A max-heap to store all the elements that are less than or equal to the effective median at any point.
A min-heap to store all the elements that are more than the effective median at any point.
Now, if the number of elements to find the median is odd, then the median is equal to the root of the max-heap. If the number of elements is even,
then the median is equal to (the root of min-heap + root of max-heap)/2.

Note that the size of both the heaps at any point will differ by at most 1.

Using the Priority_queue interface of C++, the coding part is very easy.

 ```
 
import heapq

class Solution:

    def solve(self, A):

        return self.FindMedian(A) or self.FindMedian(A[::-1]);
    
    def FindMedian(sekf,A):
        median = [A[0]];
        max_heap = []; min_heap = [A[0]];

        heapq.heapify(max_heap); heapq.heapify(min_heap);

        for i in range(1,len(A)):

            if ( len(max_heap)+len(min_heap) )%2 == 0:
                if len(max_heap)>0:
                    median = ((-1*max_heap[0]+min_heap[0])/( 2.0 ) );
                else:
                    median = min_heap[0];
            else:
                if len(max_heap)>len(min_heap):
                    median = -1*max_heap[0];
                else:
                    median = min_heap[0];
            
            num = A[i]; 
            # print(num,median)
            if float(num) == float(median):
                return 1;

            if min_heap[0] <= num:
                heapq.heappush(min_heap,num);
            else:
                heapq.heappush(max_heap,-1*num);

            if len(min_heap)-len(max_heap) > 1:
                heapq.heappush(max_heap,-1*heapq.heappop(min_heap));
            elif len(max_heap)-len(min_heap) > 1:
                heapq.heappush(min_heap,-1*heapq.heappop(max_heap));

        return 0;
 
 ```
