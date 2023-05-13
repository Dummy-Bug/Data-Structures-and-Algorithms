# https://practice.geeksforgeeks.org/problems/minimum-platforms-1587115620/1#
class Solution:    
    
    def minimumPlatform(self,n,arr,dep):
        
        arr.sort()
        dep.sort()
        
        
        j = 0 ; plateforms = 0; ans = 0
        i = 0
        while i < n and j < n:
            
            if arr[i] <= dep[j]:
                plateforms += 1
                i = i + 1
            
            else:
                plateforms -=1 
                j = j + 1
            
            ans = max(ans,plateforms)
        
        return ans