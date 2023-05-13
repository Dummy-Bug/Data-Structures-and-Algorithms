https://leetcode.com/problems/palindrome-partitioning/description/

### Problem Description 

Given a string s, partition s such that every 
substring
 of the partition is a 
palindrome
. Return all possible palindrome partitioning of s.

 

Example 1:

Input: s = "aab"
Output: [["a","a","b"],["aa","b"]]
Example 2:

Input: s = "a"
Output: [["a"]]
```

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
        
```


```


class Solution {
    public List<List<String>> partition(String s) {
        int len = s.length();
        boolean[][] dp = new boolean[len][len];
        List<List<String>> result = new ArrayList<>();
        dfs(result, s, 0, new ArrayList<>(), dp);
        return result;
    }

    void dfs(List<List<String>> result, String s, int start, List<String> currentList, boolean[][] dp) {
        if (start >= s.length()) result.add(new ArrayList<>(currentList));
        for (int end = start; end < s.length(); end++) {
            if (s.charAt(start) == s.charAt(end) && (end - start <= 2 || dp[start + 1][end - 1])) {
                dp[start][end] = true;
                currentList.add(s.substring(start, end + 1));
                dfs(result, s, end + 1, currentList, dp);
                currentList.remove(currentList.size() - 1);
            }
        }
    }
}
```
