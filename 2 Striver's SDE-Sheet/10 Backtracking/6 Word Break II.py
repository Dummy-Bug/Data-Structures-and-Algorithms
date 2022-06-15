# https://leetcode.com/problems/word-break-ii/
class Solution:
    
    def __init__(self):
        self.result = []
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        
        word_set = set(wordDict)
        
        self.helper(s,word_set,[],0)
        
        return self.result
    
    def helper(self,s,word_set,curr,start_index):
        
        if start_index == len(s):

            string = ''
            for i  in range(len(curr)):
                string = string + curr[i]
                if i < len(curr)-1: # as we don't want space after last word
                    string += ' '
            # print(string)
            self.result.append(string)
            return 
        
        
        for i in range(start_index,len(s)):

            substring = ''
            
            for char in range(start_index,i+1):
                substring = substring + s[char]
            # print(substring)
            if substring in word_set:# if prefix is in dictionary check for sufffix 
                
                curr.append(substring)
                self.helper(s,word_set,curr,i+1)
                curr.pop()
                
        