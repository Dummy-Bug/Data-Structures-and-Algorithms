### Next Permutation

https://www.interviewbit.com/problems/next-permutation/

**Hint**

You can try out a few test cases to see what the pattern is or what exactly is the flow of numbers from the initial sequence to the final sequence.


**Solution Approach**

It might help to write down the next permutation on paper to see how and when the sequence changes.

You’ll realize the following pattern :

The suffix which gets affected is in descending order before the change.

A swap with the smaller element happens, and then we reverse the affected suffix.

    1 2 3 -> 1 3 2   // Suffix being just the 3. 

    1 2 3 6 5 4  -> 1 2 4 3 5 6 // Suffix being 6 5 4 in this case.
    
    
 ``` 
 
 class Solution:

    def reverse(self,nums,start_index):
        
        end_index = len(nums)-1;
        
        while start_index <= end_index:
            
            temp = nums[start_index]
            nums[start_index] = nums[end_index]
            nums[end_index] = temp
            
            start_index += 1;
            end_index   -= 1;
        return nums

    def nextPermutation(self, A):

        n = len(A);break_index = -1;

        for i in range(n-2,-1,-1):
            if A[i] < A[i+1]:
                break_index = i;
                break;
        else:
            return A[::-1]
        
        for i in range(n-1,-1,-1):
            if A[break_index] < A[i]:
                temp = A[break_index];
                A[break_index] = A[i];
                A[i] = temp;
                break;
        
        return self.reverse(A,break_index+1)
 


 
 
 ```
