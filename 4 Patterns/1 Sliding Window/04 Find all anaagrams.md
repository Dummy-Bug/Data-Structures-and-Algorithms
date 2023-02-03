### Problem Description 

https://leetcode.com/problems/find-all-anagrams-in-a-string/
    
Given two strings s and p, return an array of all the start indices of p's anagrams in s. You may return the answer in any order.

An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original 
letters exactly once.

 

Example 1:

Input: s = "cbaebabacd", p = "abc"
Output: [0,6]
Explanation:
The substring with start index = 0 is "cba", which is an anagram of "abc".
The substring with start index = 6 is "bac", which is an anagram of "abc".
Example 2:

Input: s = "abab", p = "ab"
Output: [0,1,2]
Explanation:
The substring with start index = 0 is "ab", which is an anagram of "ab".
The substring with start index = 1 is "ba", which is an anagram of "ab".
The substring with start index = 2 is "ab", which is an anagram of "ab".
 

Constraints:

1 <= s.length, p.length <= 3 * 104
s and p consist of lowercase English letters.

**Python Code**

```


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
    
    
  ```

 **Java Code**
 
 ```
 
 class Solution 
{
    public List<Integer> findAnagrams(String s, String p) 
    {
        List<Integer> result = new ArrayList<Integer>();
        HashMap<Integer,Integer> Hash_map = new HashMap<>();
        
        int unique_count = 0;
        
        for (int i = 0; i<p.length();i++)
        {
            int curr_char = p.charAt(i);
            
            if(!Hash_map.containsKey(curr_char) )
            {
                Hash_map.put(curr_char,0);
                unique_count += 1; 
            }
            Hash_map.put(curr_char,Hash_map.get(curr_char) + 1);
        }
        
        int i = 0; int j = 0;
        
        while (j<s.length())
        {
            int curr_char = s.charAt(j);
            
            if ( Hash_map.containsKey(curr_char) )
            {
                Hash_map.put( curr_char,Hash_map.get(curr_char)-1 );
                if ( Hash_map.get(curr_char) == 0 )
                {
                    unique_count -= 1;
                }
            }
            
            if (j-i+1 < p.length())
            {
                j += 1;
            }
            else
            {
                if (unique_count == 0)
                {
                    result.add(i);
                }
                int last_char = s.charAt(i);
                if (Hash_map.containsKey(last_char))
                {
                    if ( Hash_map.get(last_char) == 0 )
                    {
                        unique_count += 1;
                    }
                    Hash_map.put(last_char,Hash_map.get(last_char)+1);
                }
            i += 1; j += 1;
            }
            
        }
    return result ;
    }
}
 
 ```
