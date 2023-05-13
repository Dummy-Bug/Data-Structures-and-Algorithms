# https://leetcode.com/problems/global-and-local-inversions/
# O(N^2)
class Solution {
    public boolean isIdealPermutation(int[] A) {
        for (int i = 0; i < A.length; i++) {
            for (int j = i + 2; j < A.length; j++) {
                if (A[j] < A[i]) {
                    return false;
                }
            }
        }
        return true;
    }
}

# O(N)
class Solution:
    def isIdealPermutation(self, nums: List[int]) -> bool:
    
        for i , num in enumerate(nums):
            
            if abs(nums[i] - i) > 1: # if deviation > 1 then it is no longer a local inversion.
                return False
        return True