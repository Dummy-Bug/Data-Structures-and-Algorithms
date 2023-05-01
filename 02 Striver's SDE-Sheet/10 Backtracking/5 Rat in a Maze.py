# https://practice.geeksforgeeks.org/problems/rat-in-a-maze-problem/1#
class Solution:
    def __init__(self):
        
        self.result = []
    def findPath(self, matrix, n):
        
        self.color  = [['white' for j in range(n)] for i in range(n)]

        self.backtrack(matrix,0,0,n,"")
        
        if not self.result:
            return [-1]
        return self.result
        
    def backtrack(self,matrix,u,v,n,path):

        # This should be above all as last cell may also contain 0
        if self.color[u][v] != 'white' or matrix[u][v] == 0:
            return 
        
        if u == n-1 and v == n-1 :
            self.result.append(path)
            return
        
        self.color[u][v] = 'grey'
        
        # follow the order DLRU so that output is in lexecographical order
        if u<n-1:
            self.backtrack(matrix,u+1,v,n,path+'D')
 
        if v>0:
            self.backtrack(matrix,u,v-1,n,path+'L')

        if v<n-1:
            self.backtrack(matrix,u,v+1,n,path+'R')

        if u>0:
            self.backtrack(matrix,u-1,v,n,path+'U')
            
        self.color[u][v] = 'white'
        return  