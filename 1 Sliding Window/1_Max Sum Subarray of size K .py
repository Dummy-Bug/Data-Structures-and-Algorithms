#User function Template for python3
class Solution:
    def maximumSumSubarray (self,k,arr,n):
        current_sum = 0
        i = 0
        
        while i < k:
            current_sum += arr[i]
            i = i + 1
        max_sum = current_sum
        current_sum = current_sum - arr[0]
        
        i = 1
        while i <= (n-k):
            
            current_sum += arr[k+i-1]
            max_sum = max(current_sum,max_sum)
            current_sum  = current_sum - arr[i]
            i = i + 1
            
        return max_sum