class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        
        dx = {}
        unique_count = 0
        for i in range(len(p)):
            if p[i] not in dx:
                dx[p[i]] = 1
                unique_count += 1
            else:
                dx[p[i]] += 1
                
        i = j = 0
        indices = []
        
        while j < len(s):
            
            if s[j] in dx:
                dx[s[j]] -= 1
                
                if dx[s[j]] == 0: # if any of the character count reaches zero  reduce count of unique characters
                    unique_count = unique_count - 1
                    
                if unique_count == 0: # if all unique characters count hit zero add the index tp index array
                    indices.append(i)
                    
            if j < len(p) - 1: # if j is less than window size 
                j = j + 1 
                continue
            else:
                if s[i] in dx:
                    if dx[s[i]] == 0:
                        unique_count += 1
                    dx[s[i]] += 1
            i = i + 1
            j = j + 1
        return indices
                    