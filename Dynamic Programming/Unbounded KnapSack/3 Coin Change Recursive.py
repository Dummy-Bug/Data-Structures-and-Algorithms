class Solution:
    def count(self, S, m, n): 
        # very similer to finding the number of subsets problem
        return self.CoinChange(S,m,n)
    
    def CoinChange(self,arr,m,n):
        
        if m == 0 and n > 0: # no success if we have still some cents left 
            return 0 
            
        if n == 0: # if we have zero cents left return a success 
            return 1
        
        elif arr[m-1] <= n:
            taken     = self.CoinChange(arr,m,n-arr[m-1])
            not_taken = self.CoinChange(arr,m-1,n)
            
            return taken + not_taken
        else:
            return self.CoinChange(arr,m-1,n)