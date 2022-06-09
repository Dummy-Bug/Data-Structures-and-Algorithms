# https://leetcode.com/problems/remove-palindromic-subsequences/

class Solution:
    def removePalindromeSub(self, s: str) -> int:
        
        i = 0
        j = len(s)-1
        
        while i <= j:
            
            if s[i] != s[j]:
                return 2
            
            i = i + 1
            j = j - 1
        
        return 1