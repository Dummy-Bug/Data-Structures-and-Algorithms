### Subsets with Duplicate Values

https://leetcode.com/problems/subsets-ii/


```

class Solution:

	def subsetsWithDup(self, A):

        self.Subsets  = [];

        self.helper(sorted(A),0,[]);
        return sorted(self.Subsets)
    
    def helper(self,arr,curr_index,curr_stack):

        self.Subsets.append(list(curr_stack));

        for i in range(curr_index,len(arr)):

            if i != curr_index and arr[i] == arr[i-1]:
                continue;

            curr_stack.append(arr[i]);
            self.helper(arr,i+1,curr_stack);
            curr_stack.pop();
            
        


```
