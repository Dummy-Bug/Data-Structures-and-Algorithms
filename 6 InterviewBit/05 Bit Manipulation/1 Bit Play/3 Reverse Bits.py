class Solution:

    def reverse(self, A):

        ans = 0;
        i = 0 ; j = 31;

        while i <= j:

            value = self.BitValue(A,i);
            ans   = ans + (1<<j)*value;
            value = self.BitValue(A,j);
            ans   = ans + (1<<i)*value;

            i = i + 1;
            j = j - 1;
        
        return ans;
    
    def BitValue(self,n,i):

        if (n>>i)&1 == 1:
            return 1;
        else:
            return 0;