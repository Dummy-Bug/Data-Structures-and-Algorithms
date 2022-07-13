class Solution:

    def singleNumber(self, A):

        xor = 0;

        for i in range(len(A)):

            xor = xor^A[i];
        
        return xor;