https://leetcode.com/problems/reverse-string/

### Problem Description

Write a function that reverses a string. The input string is given as an array of characters s.

You must do this by modifying the input array in-place with O(1) extra memory.

 

Example 1:

Input: s = ["h","e","l","l","o"]
Output: ["o","l","l","e","h"]
Example 2:

Input: s = ["H","a","n","n","a","h"]
Output: ["h","a","n","n","a","H"]
 

Constraints:

1 <= s.length <= 105
s[i] is a printable ascii character

```

class Solution {
    public void helper(char[] char_arr,int p1,int p2){
        char temp = ' ';
        temp = char_arr[p1];
        char_arr[p1] = char_arr[p2];
        char_arr[p2] = temp;
    }
    public void reverseString(char[] s) {
        int p1 = 0,p2 = s.length-1;
        while (p1<p2){
            helper(s,p1,p2);
            p1 += 1;
            p2 -= 1;
        }
    }
}

```
