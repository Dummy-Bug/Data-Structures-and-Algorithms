class Solution:
    
	def minDifference(self, arr, n):
	  
	    temp = [[-1 for j in range(sum(arr)+1)] for i in range(n+1)]
	    
	    # first set is whole array initially and 2nd set is empty
	    # using DP make the decision if element should be removed from set1 and 
	    # add it to set2 if removed 
	    
		return self.diff(arr,n,sum(arr),0,temp)
	
	def diff(self,arr,n,s1,s2,dp):
	    
	    if n == 0: # if no element left in the array return the difference
	        return abs(s1-s2)
	        
	    if dp[n][s1] != -1:# lookup in the dp table
	        return dp[n][s1]
	        
	    if s2 <= s1: # trivial step of 0/1 knapsack
	        
	        included     = self.diff(arr,n-1,s1 - arr[n-1],s2 + arr[n-1],dp)
	        not_included = self.diff(arr,n-1,s1,s2,dp)
	        
	        dp[n][s1]    = min(included,not_included)
	        return dp[n][s1]
	        
	    else: # if sum1 is lesser then return the difference 
	        dp[n][s1] =  abs(s2 - s1)
	        return dp[n][s1]
