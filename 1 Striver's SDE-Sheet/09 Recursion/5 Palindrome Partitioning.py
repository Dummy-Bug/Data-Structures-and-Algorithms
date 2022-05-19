# https://leetcode.com/problems/palindrome-partitioning/
class Solution:
    
    def __init__(self):
        
        self.curr_set = []
        self.result   = []
        
    def partition(self, s: str) -> List[List[str]]:
    
        self.helper(s,0,len(s),"",0)
        
        return self.result
    
    def helper(self,s,start_index,n,substring,n_char):
        
        if start_index == n: # means we have completed the traversal of whole string 
                             # so store all the palindrome substrings that we have chosen
            self.result.append(list(self.curr_set))
            return
            
        for i in range(start_index,n):
            
            substring = s[start_index:i+1]
            
            if self.isPalindrome(substring):
                
                self.curr_set.append(substring)
                self.helper(s,i+1,n,substring,n_char)
                self.curr_set.pop()

    def isPalindrome(self,string):
        
        string = list(string)
        return string == string[::-1]
        
        
        