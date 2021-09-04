class Solution:
    def findPath(self, matrix, n):
        
        self.color  = [['white' for j in range(n)] for i in range(n)]
        self.result = []
        if  matrix[n-1][n-1] == 0:
            return []
        self.backtrack(matrix,0,0,n,"")
        return sorted(self.result)
        
    def backtrack(self,matrix,u,v,n,path):
        
        if self.color[u][v] != 'white' or matrix[u][v] == 0:
            return 
        if u == n-1 and v == n-1 :
            self.result.append(path)
            return
        
        self.color[u][v] = 'grey'
        
        if u>0:
            self.backtrack(matrix,u-1,v,n,path+'U')
        if u<n-1:
            self.backtrack(matrix,u+1,v,n,path+'D')
        if v>0:
            self.backtrack(matrix,u,v-1,n,path+'L')
        if v<n-1:
            self.backtrack(matrix,u,v+1,n,path+'R')
            
        self.color[u][v] = 'white'
        return