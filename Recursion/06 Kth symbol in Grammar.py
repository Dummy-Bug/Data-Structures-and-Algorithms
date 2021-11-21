class Solution:
    def kthGrammar(self, n: int, k: int) -> int:
        
        if n == 1 and k == 1:
            return 0
        
        length_of_nth_row = 2**(n-1) # observe by dry running some examples.
        
        mid = length_of_nth_row//2 
        
        if k <= mid: # if kth index lies on left side of half of the row.
            
            return self.kthGrammar(n-1,k) # first half of nth row is exactly same as that of (n-1)th row.
            
        else:
            
            if self.kthGrammar(n-1,k-mid): # 2nd half of nth row is nothing but complement of (n-1)th row. 
                return 0 # toggle the bits.
                     
            return 1
            
        