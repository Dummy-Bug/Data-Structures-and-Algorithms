class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]):
        i, j = 0, 0
        result = float("inf")
        curr_sum = 0
        
        while j < len(nums):
            curr_sum += nums[j]
            while curr_sum >= target:
                result = min(result,j-i+1)
                curr_sum = curr_sum - nums[i]
                i = i + 1
            j = j + 1
        if result == float("inf"):
            return 0
        return result