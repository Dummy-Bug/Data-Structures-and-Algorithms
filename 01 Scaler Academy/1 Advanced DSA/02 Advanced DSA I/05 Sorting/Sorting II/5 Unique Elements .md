### Problem Description

You are given an array A of N elements. You have to make all elements unique. To do so, in one step you can increase any number by one.

Find the minimum number of steps.



Problem Constraints
1 <= N <= 105
1 <= A[i] <= 109



Input Format
The only argument given is an Array A, having N integers.



Output Format
Return the minimum number of steps required to make all elements unique.



Example Input
Input 1:

 A = [1, 1, 3]
Input 2:

 A = [2, 4, 5]


Example Output
Output 1:

 1
Output 2:

 0


Example Explanation
Explanation 1:

 We can increase the value of 1st element by 1 in 1 step and will get all unique elements. i.e [2, 1, 3].
Explanation 2:

 All elements are distinct.

```

class Solution:
    def minIncrementForUnique(self, nums: List[int]) -> int:
        
        map_array = [False]*(10**6);
        
        for i in range(len(nums)):
            
            map_array[nums[i]] = True;
        
        nums.sort(); moves_count = 0;
        prev_max = 0;
        
        for i in range(1,len(nums)):
            
            if nums[i] == nums[i-1]:

                prev_max = max(prev_max,nums[i]);
                
                while map_array[prev_max] != False:
                    
                    prev_max += 1;
                    
                map_array[prev_max] = True;
                moves_count += (prev_max-nums[i]);
        
        return moves_count; 

```

**Without Map --Check LeetCode--

```

class Solution:

    def solve(self, nums):

        nums.sort()
        max_val = nums[-1]
        nums.append(len(nums) + max_val)

        moves = taken = 0
        for i in range(1, len(nums)):
            if nums[i - 1] == nums[i]:
                taken += 1
                moves -= nums[i]
            else:
                give = min(taken, nums[i] - nums[i - 1] - 1)
                moves += give * (give + 1) // 2 + give * nums[i - 1]
                taken -= give

        return moves

```
