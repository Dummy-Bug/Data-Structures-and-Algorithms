### Print all unique Permutations

https://leetcode.com/problems/permutations/

**Using TempList**

```

class Solution {
public List<List<Integer>> permute(int[] nums) {
   ArrayList<List<Integer> > list = new ArrayList<List<Integer>>();
   backtrack(list, new ArrayList<>(), nums);
   return list;
}

private void backtrack(List<List<Integer>> list, List<Integer> tempList, int [] nums){
   if(tempList.size() == nums.length){
      list.add(new ArrayList<>(tempList));
   } else{
      for(int i = 0; i < nums.length; i++){ 
         if(tempList.contains(nums[i])) continue; // element already exists, skip
         tempList.add(nums[i]);
         backtrack(list, tempList, nums);
         tempList.remove(tempList.size() - 1);
      }
   }
} 
}

```

**Using Swaping method**

```

class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        
        # Think weather I can take a particular element at a particular place.

        result  = []
        self.helper(nums,0,result)
        
        return result
    
    def helper(self,nums,start_index,result):
        
        if start_index == len(nums):
            
            result.append(list(nums)) # Add the current state of nums
            
            
        for i in range(start_index,len(nums)):
            
            # swap each element one by one with starting_index
            nums[start_index], nums[i] = nums[i], nums[start_index]
            self.helper(nums,start_index+1,result)
            nums[start_index], nums[i] = nums[i], nums[start_index]
            # revert back the changes 
      
      ```
