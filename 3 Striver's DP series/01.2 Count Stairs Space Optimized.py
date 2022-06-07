# https://practice.geeksforgeeks.org/problems/reach-the-nth-point5433/1/#

class Solution:
	def nthPoint(self,n):
		
		mod = 10**9 + 7
		first_prev = 1; 
		second_prev = 1
		
		for curr in range(2,n+1):
		    
		    curr = (first_prev + second_prev)%mod
		    
		    second_prev = first_prev
		    first_prev  = curr
		
		return first_prev