class Solution:

    def divide(self, A, B):

        if A == 0:
            return 0
        INT_MAX = (1<<31)-1 ; INT_MIN = -(1<<31)
        n = A ;m = B
        
        sign = 1
        if (A < 0 and B > 0) or (A > 0 and B < 0):
            sign = -1
        n = abs(n) ; m = abs(m)
        
        ans = 0 ; temp = 0
        
        for i in range(31, -1, -1):
            if temp + (m << i) <= n:
                temp = temp + (m << i); # Bewware of Operator Presednece;
                ans  = ans | (1 << i);
        if sign < 0: 
            ans = -ans;
        
        if ans >= INT_MAX :
            return INT_MAX
        return ans