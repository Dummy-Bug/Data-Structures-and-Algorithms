class Solution:

    def solve(self, A):
        
        xor = 0;
        for i in range(len(A)):
            
            occurrence = (i+1)*(len(A)-i)
            
            if occurrence%2 != 0:
                xor = xor^A[i];
        
        return xor
            
