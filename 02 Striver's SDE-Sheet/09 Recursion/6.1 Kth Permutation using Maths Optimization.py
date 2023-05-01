# https://leetcode.com/problems/permutation-sequence/
    
class Solution:
    
    def __init__(self):
        self.s = ""
    def getPermutation(self, n: int, k: int) -> str:
        
        if n == 1:
            return "1"
        
        fact_list = []
        
        for i in range(1,n+1):
            
            fact_list.append(i)
        
        # print(fact_list)
        
        k = k - 1 # because we will consider Zero based indices
        self.helper(fact_list,k)
        return self.s
    
    def helper(self,nums,k):
        
        if len(nums) == 1:
            
            self.s = self.s + str(nums[0])
            return 
        
        
        size_of_each_block = self.fact(len(nums)-1)
        block_number = k//size_of_each_block
        
        curr_number  = nums[block_number]
        self.s = self.s + str(curr_number)
        nums.remove(curr_number)
        
        self.helper(nums,k%size_of_each_block)
    
    def fact(self,n):
        
        if n == 1 or n == 0:
            return 1
        
        return n*self.fact(n-1)