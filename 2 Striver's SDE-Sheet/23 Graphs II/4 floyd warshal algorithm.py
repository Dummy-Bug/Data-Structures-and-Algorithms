# https://practice.geeksforgeeks.org/problems/implementing-floyd-warshall2042/1#

class Solution:
	def shortest_distance(self, matrix):
		
		# Here -1 entry means distance is Infinity
		# if it was float('inf') we would not use if elif
		
		for k in range(len(matrix)):
		    for i in range(len(matrix)):
		        for j in range(len(matrix[0])):
		            

		            
		            if matrix[i][k] == -1 or matrix[k][j] == -1:
		                continue 
		            
		            if matrix[i][j] == -1:
		                matrix[i][j] = matrix[i][k] + matrix[k][j]
		            else:
		                matrix[i][j] = min(matrix[i][j],matrix[i][k]+matrix[k][j])