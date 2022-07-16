class Solution:

    def solve(self, A):
        
        msb = None;
        for i in range(31,-1,-1):
            if (A>>i)&1 == 1:
                msb = i;
                break;
        result = 0;
        
        for i in range(msb+1):
            
            if (A>>i)&1 != 1:
                result += 1<<i;
        
        return result;