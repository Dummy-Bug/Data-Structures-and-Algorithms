# https://practice.geeksforgeeks.org/problems/reach-the-nth-point5433/1/#

class Solution:
	def nthPoint(self,n):
		
		dp = [None for i in range(n+1)]
		
		dp[0] = 1 # This is kinda not intiutive
		          # as 0 is not possible bcz n is alwyas >= 1
		dp[1] = 1
		
		for step in range(2,n+1):
		    
		    dp[step] = (dp[step-1] + dp[step-2])%(10**9+7)
		   
# 		print(dp)
		return dp[n]