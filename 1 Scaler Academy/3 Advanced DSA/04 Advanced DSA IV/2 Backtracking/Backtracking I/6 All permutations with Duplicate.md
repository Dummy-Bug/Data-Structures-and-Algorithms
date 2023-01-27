### Print Unique Permutations

https://leetcode.com/problems/permutations-ii/submissions/



```
class Solution:
    # @param A : list of integers
    # @return a list of list of integers
    def permute(self, A):
        allPerms = []
        generatePerms(A, [], set(), allPerms)
        return allPerms

def generatePerms(arr,currentPerm,usedInds,allPerms):
    if len(currentPerm) == len(arr): 
        allPerms.append([num for num in currentPerm])
    usedVals = set()
    # try all possible elements for the current position
    for i in range(len(arr)):
        if not i in usedInds and not arr[i] in usedVals:  # second check to avoid duplicates
            usedVals.add(arr[i])
            usedInds.add(i)
            currentPerm.append(arr[i])
            generatePerms(arr, currentPerm, usedInds, allPerms)
            usedInds.remove(i)
            currentPerm.pop()
            
 ```


**LeetCode has better explanations and solutions**


```

class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        
        results = []
        def bt(start):
            if start == len(nums):
                results.append(nums[:])
                return
            
            lookup = set()
            
            for i in range(start,len(nums)):
                if nums[i] not in lookup:
                    nums[start], nums[i]=  nums[i],nums[start]
                    bt(start+1)
                    nums[start], nums[i]=  nums[i],nums[start]
                    lookup.add(nums[i])
        
        bt(0)
        return results
        
     ```
