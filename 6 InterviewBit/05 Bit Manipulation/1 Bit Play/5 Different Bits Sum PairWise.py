class Solution:

	def cntBits(self, A):

        result = 0;mod = 10**9 + 7;
        for i in range(31):

            setbits = unsetbits = 0;

            for j in range(len(A)):

                if self.CheckBits(A[j],i):
                    setbits += 1;
            
            unsetbits = len(A)-setbits;
            
            countribution = (setbits*unsetbits)%mod
            result = (result + countribution)%mod;
        
        return (2*result)%mod;
    
    def CheckBits(self,n,i):

        if (n>>i)&1 == 1:
            return True
        else:
            return False