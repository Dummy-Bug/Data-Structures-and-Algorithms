### Problem Description 

Given a string s, find the length of the longest 
substring
 without repeating characters.

 

Example 1:

Input: s = "abcabcbb"
Output: 3
Explanation: The answer is "abc", with the length of 3.
Example 2:

Input: s = "bbbbb"
Output: 1
Explanation: The answer is "b", with the length of 1.
Example 3:

Input: s = "pwwkew"
Output: 3
Explanation: The answer is "wke", with the length of 3.
Notice that the answer must be a substring, "pwke" is a subsequence and not a substring.
 

Constraints:

0 <= s.length <= 5 * 104
s consists of English letters, digits, symbols and spaces.


```

class Solution:

    def lengthOfLongestSubstring(self, string):
        
        freq_map = dict();
        
        for character in string:
            if character not in freq_map:
                freq_map[character] = 0;
        
        i = j = 0; 
        max_length = 0;
        
        while j<len(string):
            
            
            if freq_map[string[j]] == 0:
                max_length = max(max_length,j-i+1);
                freq_map[string[j]] += 1;
                j += 1;
                continue;
                
            while freq_map[string[j]] != 0:
                freq_map[string[i]] -= 1;
                i += 1;
 
        
        return max_length;

```
