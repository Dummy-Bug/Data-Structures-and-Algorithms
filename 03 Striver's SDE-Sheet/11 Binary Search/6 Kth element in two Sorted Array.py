# https://practice.geeksforgeeks.org/problems/k-th-element-of-two-sorted-array1317/1#

class Solution:
    def kthElement(self,  arr1, arr2, n, m, k):
        
        if n > m:
            return self.kthElement(arr2,arr1,m,n,k)
        
        low  = 0
        high = n
        
        
        while low <= high:
            
            cut1 = (low+high)>>1
            
            cut2 = k - cut1
            
            if cut2 < 0:
                high = cut1 - 1
                continue
            if cut2 > m: 
                low = cut1 + 1
                continue
            
            l1 = arr1[cut1-1] if cut1 != 0 else float('-inf')
            l2 = arr2[cut2-1] if cut2 != 0 else float('-inf')
            
            r1 = arr1[cut1] if cut1 != n else float('inf')
            r2 = arr2[cut2] if cut2 != m else float('inf')
            
            if l1 <= r2 and l2 <= r1:
                
                return max(l1,l2)
            
            if l1 > r2:
                high = cut1 -1 
            else:
                low = cut1 + 1