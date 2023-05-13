### Problem Description 

Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]] such that i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0.

Notice that the solution set must not contain duplicate triplets.

 

Example 1:

Input: nums = [-1,0,1,2,-1,-4]
Output: [[-1,-1,2],[-1,0,1]]
Explanation: 
nums[0] + nums[1] + nums[2] = (-1) + 0 + 1 = 0.
nums[1] + nums[2] + nums[4] = 0 + 1 + (-1) = 0.
nums[0] + nums[3] + nums[4] = (-1) + 2 + (-1) = 0.
The distinct triplets are [-1,0,1] and [-1,-1,2].
Notice that the order of the output and the order of the triplets does not matter.
Example 2:

Input: nums = [0,1,1]
Output: []
Explanation: The only possible triplet does not sum up to 0.
Example 3:

Input: nums = [0,0,0]
Output: [[0,0,0]]
Explanation: The only possible triplet sums up to 0.
 

Constraints:

3 <= nums.length <= 3000
-105 <= nums[i] <= 105


```

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        
        result = []
        nums.sort() # By this it will be easy to skip over the elements
        
        for i in range(len(nums)-2): # This loop wil run only n-3
            
            
            if i > 0 and nums[i] == nums[i-1]: # It is the most intitutive condition 
                # we have found all the possible triplits with nums[i-1] and now if nums[i] == nums[i-1]: then it will just be repeatition
                continue
            
            # Reduce the problem to 2Sum by fixing one element "nums[i]".
            
            low,high = i+1,len(nums)-1
            
            while low < high:
                
                triplet_sum = nums[low] + nums[high] + nums[i] 
                # print(triplet_sum)
                if triplet_sum < 0: # since we want sum = 0 hence we need to increase our sum
                    low += 1
                
                if triplet_sum > 0:# since we want sum = 0 hence we need to decrease our sum
                    high -= 1
                
                if triplet_sum == 0: # we have the desired sum
                    print(triplet_sum)
                    result.append([nums[i],nums[low],nums[high]])
                    
                    low  += 1
                    high -= 1
                    
                    while low < high and nums[low] == nums[low-1]: # we do not want the same element
                        low += 1                                   # bcz if nums[low] is same prev. then nums[high] will also be same to satisfy the relation 
                    while high > low and nums[high] == nums[high+1]:
                        high -= 1
        return result
                        
                        
                    
                    
                    

```
