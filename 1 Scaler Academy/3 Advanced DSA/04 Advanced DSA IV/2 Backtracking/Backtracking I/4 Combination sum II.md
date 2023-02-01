### Problem Description

Given an array of size N of candidate numbers A and a target number B. Return all unique combinations in A where the candidate numbers sums to B.

Each number in A may only be used once in the combination.

Note:

All numbers (including target) will be positive integers.
Elements in a combination (a1, a2, … , ak) must be in non-descending order. (ie, a1 ≤ a2 ≤ … ≤ ak).
The solution set must not contain duplicate combinations.
Warning:

DO NOT USE LIBRARY FUNCTION FOR GENERATING COMBINATIONS.

Example : itertools.combinations in python. If you do, we will disqualify your submission and give you penalty points.



Problem Constraints
1 <= N <= 20



Input Format
First argument is an integer array A denoting the collection of candidate numbers.
Second argument is an integer which represents the target number.



Output Format
Return all unique combinations in A where the candidate numbers sums to B.



Example Input
Input 1:

 A = [10, 1, 2, 7, 6, 1, 5]
 B = 8
Input 2:

 A = [2, 1, 3]
 B = 3


Example Output
Output 1:

 [ 
  [1, 1, 6 ],
  [1, 2, 5 ],
  [1, 7 ], 
  [2, 6 ] 
 ]
Output 2:

 [
  [1, 2 ],
  [3 ]
 ]


Example Explanation
Explanation 1:

 1 + 1 + 6 = 8
 1 + 2 + 5 = 8
 1 + 7 = 8
 2 + 6 = 8
 All the above combinations sum to 8 and are arranged in ascending order.
Explanation 2:

 1 + 2 = 3
 3 = 3
 All the above combinations sum to 3 and are arranged in ascending order.



```

class Solution:
    
    def __init__(self):
        self.combn_set = []
        self.result    = []

	def combinationSum(self, A, target):

        self.AllCombinations = [];
        self.helper(sorted(A),0,0,target)
        return sorted(self.result);
    
    def helper(self,nums,start_index,c_sum,target):
        
        if c_sum == target:
            self.result.append(list(self.combn_set))
            return 
        
        for i in range(start_index,len(nums)):
            
            if i != start_index and nums[i] == nums[i-1]:
                continue;

            if c_sum + nums[i] <= target:
                self.combn_set.append(nums[i])
                self.helper(nums,i+1,c_sum+nums[i],target)
                self.combn_set.pop()
            

```
