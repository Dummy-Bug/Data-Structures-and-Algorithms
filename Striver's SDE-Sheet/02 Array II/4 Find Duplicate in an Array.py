# Best solution is using fast and slow pointer but this is my fav solution.
# solution using negative marking was also intuitive 

class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        # Solution is not acceptable as we are changing the actual elements present in the Array.  
        i = 0
        while (1):
            
            ele = nums[i]
            if ele == nums[ele]:
                return ele
            
            else: # store the index value in array.
                nums[i] = i
                i = ele