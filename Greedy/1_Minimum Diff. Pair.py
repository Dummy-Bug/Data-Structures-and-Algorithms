class Solution:
	def minimum_difference(self, nums):
		
		nums.sort()
		result = float("inf")
		
		for i in range(1,n):
		    result = min(result,abs(nums[i-1]-nums[i]))
		return result