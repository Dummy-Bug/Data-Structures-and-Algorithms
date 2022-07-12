class Solution:
    # @param A : list of integers
    # @return a list of integers
    def maxset(self, A):
        
        curr_sum = 0; start = 0;left_index = 0;
        right_index = -1;
        max_sum  = float('-inf');
        
        for i in range(len(A)):
            
            if A[i] < 0:
                curr_sum = 0
                start = i + 1;
                continue
            
            curr_sum += A[i]
            
            if max_sum < curr_sum:
                max_sum = curr_sum
                left_index  = start;
                right_index = i;
            
            elif max_sum == curr_sum:
                if (right_index - left_index) < (i-start):
                    left_index  = start;
                    right_index = i;
 
        return A[left_index:right_index+1]