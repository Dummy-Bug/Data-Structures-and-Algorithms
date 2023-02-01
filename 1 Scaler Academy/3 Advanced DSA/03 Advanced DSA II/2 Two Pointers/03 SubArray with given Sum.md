### Problem Description

Given an array of positive integers A and an integer B, find and return first continuous subarray which adds to B.

If the answer does not exist return an array with a single element "-1".

First sub-array means the sub-array for which starting index in minimum.



Problem Constraints
1 <= length of the array <= 100000
1 <= A[i] <= 109
1 <= B <= 109



Input Format
The first argument given is the integer array A.

The second argument given is integer B.



Output Format
Return the first continuous sub-array which adds to B and if the answer does not exist return an array with a single element "-1".



Example Input
Input 1:

 A = [1, 2, 3, 4, 5]
 B = 5
Input 2:

 A = [5, 10, 20, 100, 105]
 B = 110


Example Output
Output 1:

 [2, 3]
Output 2:

 -1


Example Explanation
Explanation 1:

 [2, 3] sums up to 5.
Explanation 2:

 No subarray sums up to required number.
 
 **Solution Approach**
 
We can use 2 pointer technique to solve this problem efficiently.
We can keep pointers left and right.
we move right if our sum is < target.
we move left when sum > target. using left and right, we get our subarray.


```

class Solution:

    def solve(self, A, B):

        prefix_arr = [];prefix_arr.append(A[0]);

        for i in range(1,len(A)):
            prefix_arr.append(prefix_arr[i-1]+A[i]);
    
        i = 0; j = 0; flag = False;

        while i < len(prefix_arr) and j < len(prefix_arr):

            if i == j:
                j += 1;
                continue;
            if prefix_arr[j] == B: # to also include subArrays starting with 0th index
            
                return A[0:j+1];
            curr_sum = prefix_arr[j] - prefix_arr[i];

            if curr_sum == B:
                flag = True;
                break;
            if curr_sum < B:
                j += 1;
                continue;
            if curr_sum > B:
                i += 1;

        if flag == False:
            return [-1];
        
        temp = [];
        for k in range(i+1,j+1):
            temp.append(A[k])
        return temp
        
 ```
 
 
**Without Extra Space**


```

class Solution:
    # @param A : list of integers
    # @param B : integer
    # @return a list of integers
    def solve(self, A, B):
        n = len(A)
        i = j = 0
        list = []
        sum = A[0]
        flag = False
        
        while j < n and i < n:
            if sum == B:
                # current window sum = B
                flag = True
                break

            elif sum < B:
                # current window sum < B
                if j + 1 == n:
                    break
                j = j + 1
                sum = sum + A[j]

            else:
                # current window sum > B
                if i + 1 == n:
                    break
                i = i + 1
                sum = sum - A[i - 1]

        if flag == False:
            return [-1]

        for k in range(i, j + 1):
            list.append(A[k])

        return list


```
