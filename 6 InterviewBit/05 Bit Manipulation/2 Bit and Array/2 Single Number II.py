class Solution:
	# @param A : tuple of integers
	# @return an integer
	def singleNumber(self, A):
        
        unique_element = 0;
        
        for i in range(32):
            
            bit_count = 0;
            
            for j in range(len(A)):
                if self.checkBit(A[j],i):
                    bit_count += 1;
                
            if (bit_count%3) != 0:
                unique_element += 1<<i;
        
        return unique_element;
    
    def checkBit(self,n,i):
        if (n>>i)&1 == 1:
            return True
        return False
                