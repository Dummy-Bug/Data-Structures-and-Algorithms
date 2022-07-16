class Solution:
    def solve(self, A, B, C):
        
        B = B - 1;
        C = C - 1;
        ans = A;
        
        if (A>>B)&1 == 1:
            
            ans = ans + (1<<C) - (1<<B);
        
        if (A>>C)&1 == 1:
               
            ans = ans + (1<<B) - (1<<C);
        
        return ans