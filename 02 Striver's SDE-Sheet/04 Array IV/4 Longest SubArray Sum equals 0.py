# https://practice.geeksforgeeks.org/problems/largest-subarray-with-0-sum/1/#
class Solution:
    def maxLen(self, n, arr):
        
        largest_sum = 0
        pref_sum    = 0
        dx = dict()
        
        for i in range(len(arr)):
            
            pref_sum += arr[i]
            
            if pref_sum == 0: # if pref_sum become 0 it means whole array till ith index
                              # has sum = 0 .
                largest_sum = max(largest_sum ,i+1)
            else:
                
                if pref_sum not in dx:
                    dx[pref_sum] = i
                
                else: 
                        index = dx[pref_sum] # get the index that had the same sum     
                        largest_sum = max(largest_sum,i-index)
        
        return largest_sum