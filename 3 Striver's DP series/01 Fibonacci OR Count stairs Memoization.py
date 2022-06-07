# https://practice.geeksforgeeks.org/problems/reach-the-nth-point5433/1/#

class Solution:
	def nthPoint(self,n):
		
		dp = [None for i in range(n+1)]
		
		return self.helper(n,dp)
		
	
	def helper(self,step,dp):
	    
	    if step == 0 or step == 1:
	        return 1
	    
	    if dp[step] != None:
	        return dp[step]
	        
	    dp[step] = (self.helper(step-1,dp)+self.helper(step-2,dp))%(10**9+7)
		
		return dp[step]