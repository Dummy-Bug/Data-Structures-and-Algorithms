class Solution:
    # @param A : integer
    # @return a strings
    def solve(self, A):
        
        fact = dict()
        fact[0] = 1;
        
        for i in range(1,A+1):
            fact[i] = *fact[A-1];
        
        return fact[A]