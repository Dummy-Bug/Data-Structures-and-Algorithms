class Solution:

	def findMinXor(self, A):
        
        min_xor = float('inf');
        
        A.sort();
        
        for i in range(len(A)-1):
            min_xor = min(min_xor,A[i]^A[i+1]);
        
        return min_xor;