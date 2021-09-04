class solution:
    
    def minDifference(self, arr, n):
        # code is explained in Memiozation part
        return self.diff(arr,n,sum(arr),0)
    
    def diff(self,arr,n,s1,s2):
        
        if n == 0:
            return abs(s1-s2)
        
        if s2 <= s1:
            
            included     = self.diff(arr,n-1,s1 - arr[n-1],s2 + arr[n-1])
            not_included = self.diff(arr,n-1,s1,s2)
            
            return min(included,not_included)
        else:
            return abs(s2 - s1)
