### Problem Description 

Given a string you need to print the size of the longest possible substring that has exactly K unique characters. 
If there is no possible substring then print -1.

https://practice.geeksforgeeks.org/problems/longest-k-unique-characters-substring0853/1?utm_source=gfg&utm_medium=article&utm_campaign=bottom_sticky_on_article

Example 1:

Input:
S = "aabacbebebe", K = 3
Output: 7
Explanation: "cbebebe" is the longest 
substring with K distinct characters.
Example 2:

Input: 
S = "aaaa", K = 2
Output: -1
Explanation: There's no substring with K
distinct characters.

Your Task:
You don't need to read input or print anything. Your task is to complete the function longestKSubstr() which takes the string S and an integer 
K as input and returns the length of the longest substring with exactly K distinct characters. If there is no substring with exactly K distinct 
characters then return -1.


class Solution:
    def longestKSubstr(self, s, k):
        dx = {}
        j = i = unique_char = 0
        result = -1
        while j < len(s):
            
            if s[j] not in dx or dx[s[j]]==0:
                dx[s[j]] = 1
                unique_char += 1
            else:
                dx[s[j]] += 1
                
            if unique_char  < k:
                j = j + 1
            elif unique_char == k:
                result = max(result,j-i+1)
                j = j + 1
                
            else:
                while unique_char > k:
                    dx[s[i]] = dx[s[i]] - 1
                    if dx[s[i]] == 0:
                        unique_char -= 1
                    i = i + 1
                j = j + 1
                
        return result
