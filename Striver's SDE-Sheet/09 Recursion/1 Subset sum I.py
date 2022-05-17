# https://practice.geeksforgeeks.org/problems/subset-sums2234/1#
class Solution:
        
	def subsetSums(self, arr, N):
	    
	    result = []
	    self.helper(arr,N,0,0,result)
	    return result
	
	def helper(self,arr,n,index,subset_sum,result):
	    if index >= n:
	        result.append(subset_sum)
	        return
	    
	    subset_sum = subset_sum + arr[index]
	    self.helper(arr,n,index+1,subset_sum,result) # include the current element
	    
	    subset_sum = subset_sum - arr[index]
	    self.helper(arr,n,index+1,subset_sum,result) # do not include the element
	    
	