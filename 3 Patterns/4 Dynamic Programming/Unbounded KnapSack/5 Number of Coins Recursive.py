class Solution:
    def __init__(self):
        import sys
        sys.setrecursionlimit(10**6)
	def minCoins(self, coins, M, V):
		# make the recursion tree
		return self.helper(coins,M,V,0)
	
	def helper(self,arr,m,n,count):
	    
	    if n == 0: # if no amount left return the count of coins
	        return count
	        
	    if m == 0 and n > 0:
	        return -1 # reuturn -1 if can't found a way to make the change
	       
	    if arr[m-1] <= n:
	        
	        taken     = self.helper(arr,m,n-arr[m-1],count + 1)
	        not_taken = self.helper(arr,m-1,n,count)
	        
	        if taken == -1 or not_taken == -1: 
	            return max(taken,not_taken)
	        else:
	            return min(taken,not_taken)
	    else:
	        return self.helper(arr,m-1,n,count)