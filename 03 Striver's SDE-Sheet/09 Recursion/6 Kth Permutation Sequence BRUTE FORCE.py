# https://leetcode.com/problems/permutation-sequence/
'''
Time complexity: O(N! * N) +O(N! Log N!)
'''

class Solution:
    def getPermutation(self, n: int, k: int) -> str:
        
        
        curr_permutation = []
        
        for i in range(1,n+1):
            curr_permutation.append(i)
            
        print(curr_permutation)
        
        for i in range(1,k):
            curr_permutation = self.nextPermutation(curr_permutation)
            
        strings    = [str(integer) for integer in curr_permutation]
        kth_permutation   = "".join(strings)
        
        return kth_permutation
        
    
    def nextPermutation(self, nums: List[int]):
        
        BreakDownIndex = -1
        
        for i in range(len(nums)-1,0,-1):
            if nums[i] > nums[i-1]:
                
                BreakDownIndex = i-1
                break

        if BreakDownIndex != -1:
            
            for i in range(len(nums)-1,0,-1):
                
                if nums[i] > nums[BreakDownIndex]: # swap to get the bigger prefix than already present prefix
                    
                    nums[i] , nums[BreakDownIndex] = nums[BreakDownIndex], nums[i]
                    break
            
        i, j = BreakDownIndex + 1, len(nums)-1  # BreakDownIndex == -1 then it will become 0 and hence 
                                                # whole list will get reverse and that is what we want
            
        while i < j: # reverse the suffix or whole array 
            nums[i], nums[j] = nums[j], nums[i]
            i = i + 1
            j = j - 1
        
        return nums