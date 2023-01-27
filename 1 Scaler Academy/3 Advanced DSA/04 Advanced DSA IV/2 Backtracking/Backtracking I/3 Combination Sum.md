Problem Description
Given an array of candidate numbers A and a target number B, find all unique combinations in A where the candidate numbers sums to B.

The same repeated number may be chosen from A unlimited number of times.

Note:

1) All numbers (including target) will be positive integers.

2) Elements in a combination (a1, a2, … , ak) must be in non-descending order. (ie, a1 ≤ a2 ≤ … ≤ ak).

3) The combinations themselves must be sorted in ascending order.

4) CombinationA > CombinationB iff (a1 > b1) OR (a1 = b1 AND a2 > b2) OR ... (a1 = b1 AND a2 = b2 AND ... ai = bi AND ai+1 > bi+1)

5) The solution set must not contain duplicate combinations.



Problem Constraints
1 <= |A| <= 20

1 <= A[i] <= 50

1 <= B <= 500



Input Format
The first argument is an integer array A.

The second argument is integer B.



Output Format
Return a vector of all combinations that sum up to B.



Example Input
Input 1:

A = [2, 3]
B = 2
Input 2:

A = [2, 3, 6, 7]
B = 7


Example Output
Output 1:

[ [2] ]
Output 2:

[ [2, 2, 3] , [7] ]


Example Explanation
Explanation 1:

All possible combinations are listed.
Explanation 2:

All possible combinations are listed.



**Desi Method**

```

class Solution:
    # @param A : list of integers
    # @param B : integer
    # @return a list of list of integers
    def dfs(self, A, pos, cur, total, B, res):
        if total == B:
            if cur not in res:
                res.append(cur.copy())
            return

        if pos == len(A) or total > B: return

        # including the current element
        cur.append(A[pos])
        self.dfs(A, pos, cur, total + A[pos], B, res)

        # popping the current element
        cur.pop()
        self.dfs(A, pos + 1, cur, total, B, res)

    def combinationSum(self, A, B):
        res = []
        A.sort()

        self.dfs(A, 0, [], 0, B, res)
        # res.sort()

        return res

        # TC: O(2^B); SC: O(B)
        
   ```
   
   **All Mighty Method**
   
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
                self.helper(nums,i,c_sum+nums[i],target)
                self.combn_set.pop()
            

   
   ```
