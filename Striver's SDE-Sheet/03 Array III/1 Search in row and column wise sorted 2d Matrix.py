
# T(c) = O(n+m)
class Solution:
	def matSearch(self,matrix, N, M, X):
		
		i = 0
		j = M - 1
		
		while i < N and j > -1:
		    
		    if matrix[i][j] == X:
		        return 1
		    
		    elif matrix[i][j] > X:
		        j = j - 1
		    
		    else:
		        i = i + 1
		else:
		    return 0
		 
		
		
		
