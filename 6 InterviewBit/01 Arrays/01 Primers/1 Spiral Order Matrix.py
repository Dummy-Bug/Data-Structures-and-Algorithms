class Solution:
	# @param A : tuple of list of integers
	# @return a list of integers
	def spiralOrder(self, A):
        
        start_row = start_col = 0;
        end_row   = len(A)-1;
        end_col   = len(A[0])-1;
        spiralOrder = [];
        
        while start_row <= end_row and start_col <= end_col:
            
            # Traversing the first unvisited row. 
            for j in range(start_col,end_col+1):
                spiralOrder.append(A[start_row][j]);
            
            # Traversing the last unvisited column.
            
            for i in range(start_row+1,end_row+1):
                
                spiralOrder.append(A[i][end_col]);
            
            # Traversing the last unvisited row.
            if start_row < end_row:
                for j in range(end_col-1,start_col-1,-1):

                    spiralOrder.append(A[end_row][j]);
                
            
            # Traversing the first unvisited column.
            if start_col < end_col:
                for i in range(end_row-1,start_row,-1):

                    spiralOrder.append(A[i][start_col]);
            
            start_row += 1; start_col += 1;
            end_row   -= 1; end_col   -= 1;
        
        return spiralOrder