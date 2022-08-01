class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        dx = {}
        
        for idx, num in enumerate(nums):
            
            if target-num not in dx:
                dx[num] = idx
            
            else:
                return [idx,dx[target-num]]