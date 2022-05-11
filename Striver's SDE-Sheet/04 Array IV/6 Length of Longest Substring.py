# https://leetcode.com/problems/longest-substring-without-repeating-characters/
class Solution:
    def lengthOfLongestSubstring(self, s: str):
        
        dx = {}
        i, j, result = 0, 0, 0
        
        for char in s:
            if char not in dx:
                dx[char] = 0
                
        while j < len(s):
            
            dx[s[j]] = dx[s[j]] + 1
            
            if dx[s[j]] == 1:
                result = max(result,j-i+1)
                
            else:
                while s[i]!=s[j]:
                        dx[s[i]] = dx[s[i]] - 1
                        i = i + 1
                
                dx[s[i]] = dx[s[i]] - 1
                i = i + 1
                    
            j = j + 1
        return result