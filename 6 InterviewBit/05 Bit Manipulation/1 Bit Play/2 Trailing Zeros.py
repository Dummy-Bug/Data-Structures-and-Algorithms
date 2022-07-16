class Solution:

    def solve(self, A):
        
        count = 0;
        
        for i in range(32):
            
            if (A>>i)&1 == 1:
                return count;
            count += 1;
            