# https://www.geeksforgeeks.org/find-a-repeating-and-a-missing-number/
class Solution:
    def findTwoElement( self,nums, n):
        
        duplicate_ele , missing_ele = -1, -1
        
        for i in range(n): # consider array element as indices and mark the index visisted 
            
            index = abs(nums[i]) - 1 # range is [1,n]  instead of zero so we have to subtracy from 1
            
            if nums[index] < 0 : # if index was already visisted then it must be duplicate index
                                 # so to get the duplicate element just do index+1.
                    duplicate_ele = index + 1
            else: # if positive then index is visited only one time.
                nums[index] = -nums[index] # make the element - to mark it as visited
        
        for i in range(n):
            
            if nums[i] > 0:
                missing_ele = i + 1 
                return (duplicate_ele,missing_ele)