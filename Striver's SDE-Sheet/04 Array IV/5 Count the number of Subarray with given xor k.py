# https://www.interviewbit.com/problems/subarray-with-given-xor/
class Solution:
    # @param A : list of integers
    # @param B : integer
    # @return an integer
    def solve(self, A, B):
        dx = {}
        ans = 0
        xor = 0

        for ele in A:
            xor = xor ^ ele
            
            if xor^B in dx:
                ans+=dx[xor^B]
            if xor==B:
                ans+=1
            if xor in dx:
                dx[xor]+=1
            else:
                dx[xor]=1
        return ans
