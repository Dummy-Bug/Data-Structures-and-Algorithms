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
