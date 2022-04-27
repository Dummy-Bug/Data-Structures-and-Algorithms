# https://leetcode.com/problems/pascals-triangle/
# T(c) = O(N^2)
# S(c) = O(N) -- to make result array we are using new_list

class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        
        result = []
        for i in range(0,numRows):
            new_list = [1 for j in range(i+1)] # as this will make the result array so it's size should be equal to NumRows 
            result.append(new_list)
            
        print(result)
        
        for i in range(2,numRows): # as 0th and 1th rows are already in the desired form.
            # starting from 1st as (0th)first index is always 1 and last index is also 1 but we 
            # are alredy taking the len of prevoius array so it is automatically one less in size.
            for j in range(1,len(result[i-1])): # to get the 3rd(ith) row we have to traverse till len of 2nd(i-1) row.
                
                result[i][j] = result[i-1][j-1] + result[i-1][j]
                
        return result
        
        