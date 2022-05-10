# https://leetcode.com/problems/longest-consecutive-sequence/submissions/

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        
        st = set(nums)
        
        longest_seq = 0
        curr_seq    = 0
        
        for num in nums:
            
            if num-1 not in st: # if current element is not a part of any sequence 
                
                curr_num = num
                curr_seq = 1
                
                while curr_num+1 in st:
                    curr_seq += 1
                    curr_num += 1
                
                longest_seq = max(longest_seq,curr_seq)
        
        return longest_seq
                