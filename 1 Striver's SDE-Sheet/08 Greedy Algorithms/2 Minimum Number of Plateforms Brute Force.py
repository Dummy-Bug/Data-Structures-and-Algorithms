# https://practice.geeksforgeeks.org/problems/minimum-platforms-1587115620/1#
class Solution:    
    
    def minimumPlatform(self,n,arr,dep):

        ans = 0
        for i in range(n):
            count = 1# i think it's failing for (1,4)(0,3)(5,5)(0,5)(2,5)
            for j in range(i+1,n):
 
                if arr[i]>=arr[j] and arr[i]<=dep[j] or arr[j]>=arr[i] and arr[j]<=dep[i]:
                    
                    count += 1
            
            ans = max(count,ans)
        
        return ans