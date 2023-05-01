### Problem Description 

You are given a string s and an integer k. You can choose any character of the string and change it to any other uppercase English character.
You can perform this operation at most k times.

Return the length of the longest substring containing the same letter you can get after performing the above operations.

 https://leetcode.com/problems/longest-repeating-character-replacement/
 

Example 1:

Input: s = "ABAB", k = 2
Output: 4
Explanation: Replace the two 'A's with two 'B's or vice versa.
Example 2:

Input: s = "AABABBA", k = 1
Output: 4
Explanation: Replace the one 'A' in the middle with 'B' and form "AABBBBA".
The substring "BBBB" has the longest repeating letters, which is 4.
 

Constraints:

1 <= s.length <= 105
s consists of only uppercase English letters.
0 <= k <= s.length
Accepted
405,271
Submissions
783,660

**Approach 1: Sliding Window + Binary Search**

**Intuition**

Since the question asks us to find the longest substring length that satisfies the given conditions, we can start with generating all 
possible substrings.

Now, given a substring, we want to find out if it can be converted into a string with the same letters. Because we are allowed only 
k operations to do so, we would want to minimize the number of operations.

We can divide all the characters of the string s into two groups - fixed letters and the letters that will be changed. Fixed letters remain
unchanged. The rest of the letters would be substituted by fixed letters. To keep the number of substitutions minimum, the number of fixed 
letters must be maximum.
So, we find the character target, which occurs with the maximum frequency in the string. All other characters can now be replaced with target. 
If the count of other characters is less than or equal to  k, then this substring fulfills the condition given in the question. 
We'd call it a valid substring.


```

class Solution {
    public int characterReplacement(String s, int k) 
    {
        HashSet<Character> allLetters = new HashSet();

        // collect all unique letters
        for (int i = 0; i < s.length(); i++) {
            allLetters.add(s.charAt(i));
        }

        int maxLength = 0;
        for (Character letter : allLetters) 
        {
            int start = 0;
            int count = 0;
            // initialize a sliding window for each unique letter
            for (int end = 0; end < s.length(); end += 1) 
            {
                if (s.charAt(end) == letter) 
                {
                    // if the letter matches, increase the count
                    count += 1;
                }
                // bring start forward until the window is valid again
                while (!isWindowValid(start, end, count, k)) 
                {
                    if (s.charAt(start) == letter) 
                    {
                        // if the letter matches, decrease the count
                        count -= 1;
                    }
                    start += 1;
                }
                // at this point the window is valid, update maxLength
                maxLength = Math.max(maxLength, end + 1 - start);
            }
        }
        return maxLength;
    }

    private Boolean isWindowValid(int start, int end, int count, int k)
    {
        return end + 1 - start - count <= k;
    }
}

```


We repeat the last two steps until the window reaches the right edge of the string.


```

class Solution 
{
    public int characterReplacement(String s, int k) 
    {
        int len = s.length();
        int[] count = new int[26];
        int start = 0, maxCount = 0, maxLength = 0;
        for (int end = 0; end < len; end++) 
        {
            maxCount = Math.max(maxCount, ++count[s.charAt(end) - 'A']);
            
            while (end - start + 1 - maxCount > k) 
            {
                count[s.charAt(start) - 'A']--;
                start++;
            }
            maxLength = Math.max(maxLength, end - start + 1);
        }
        return maxLength;
    }
}

```
