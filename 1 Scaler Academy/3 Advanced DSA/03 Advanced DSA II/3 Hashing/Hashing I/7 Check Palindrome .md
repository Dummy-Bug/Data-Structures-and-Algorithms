### Problem Description

Given a string A consisting of lowercase characters.

Check if characters of the given string can be rearranged to form a palindrome.

Return 1 if it is possible to rearrange the characters of the string A such that it becomes a palindrome else return 0.



Problem Constraints
1 <= |A| <= 105

A consists only of lower-case characters.



Input Format
First argument is an string A.



Output Format
Return 1 if it is possible to rearrange the characters of the string A such that it becomes a palindrome else return 0.



Example Input
Input 1:

 A = "abcde"
Input 2:

 A = "abbaee"


Example Output
Output 1:

 0
Output 2:

 1


Example Explanation
Explanation 1:

 No possible rearrangement to make the string palindrome.
Explanation 2:

 Given string "abbaee" can be rearranged to "aebbea" to form a palindrome.

**Approach**

A set of characters can form a palindrome if at most one character occurs odd number of times and all characters occur even number of times.

We can do it in O(|A|) time using a count array.
Following are detailed steps.

Create a count array of alphabet size which is typically 26. Initialize all values of count array as 0.
Traverse the given string and increment count of every character.
Traverse the count array and if the count array has more than one odd values, return false. Otherwise return true.

```

class Solution:

    def solve(self, A):

        length = len(A);

        freq_map = dict();

        for character in A:
            if character not in freq_map:
                freq_map[character] = 0;
            freq_map[character] += 1;
        # print(length,freq_map);
        if length%2 == 0:
            for frequency in freq_map.values():
                if (frequency%2) != 0:
                    return 0;
            else:
                return 1;
        else:
            odd_count = 0;
            for frequency in freq_map.values():
                if (frequency%2) != 0:
                    odd_count += 1;
                    
                    if (odd_count > 1):
                        return 0;
            else:
                return 1;

```
