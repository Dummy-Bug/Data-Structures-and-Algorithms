### Problem Description 

Given a string s, find the first non-repeating character in it and return its index. If it does not exist, return -1.

```

class Solution:
    def firstUniqChar(self, s: str) -> int:
        
        freq_array  = [0]*26;
        index_array = [0]*26;
        
        for i in range(len(s)):
            
            char = s[i];
            
            freq_array[ord(char)-97] += 1;
            index_array[ord(char)-97] = i;
            
        
        for i in range(len(s)):
            
            char = s[i];
            
            if freq_array[ord(char)-97] == 1:
                return index_array[ord(char)-97];
        return -1;
            
        

```
