### Problem Description 

A phrase is a palindrome if, after converting all uppercase letters into lowercase letters and removing all non-alphanumeric characters, it reads the same forward and backward. Alphanumeric characters include letters and numbers.

Given a string s, return true if it is a palindrome, or false otherwise.

 

Example 1:

Input: s = "A man, a plan, a canal: Panama"
Output: true
Explanation: "amanaplanacanalpanama" is a palindrome.
Example 2:

Input: s = "race a car"
Output: false
Explanation: "raceacar" is not a palindrome.
Example 3:

Input: s = " "
Output: true
Explanation: s is an empty string "" after removing non-alphanumeric characters.
Since an empty string reads the same forward and backward, it is a palindrome.
 

Constraints:

1 <= s.length <= 2 * 105
s consists only of printable ASCII characters.


```

class Solution:
    def isPalindrome(self, s: str) -> bool:
        
        i , j = 0 , len(s)-1
        
        while i < j :
            if s[i].isalpha() and s[j].isalpha():
                if s[i].lower() != s[j].lower():
                    return False
                else:
                    i = i + 1
                    j = j - 1
                    
            
            elif not s[i].isalpha() and not s[i].isdigit():
                i = i + 1
            elif not s[j].isalpha() and not s[j].isdigit():
                j = j - 1
            else:
                if s[i] != s[j]:
                    return False
                else:
                    i = i + 1
                    j = j - 1 
        
        return True
                
                
```
