### Problem Description 

Given an array of strings strs, group the anagrams together. You can return the answer in any order.

An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.

 

Example 1:

Input: strs = ["eat","tea","tan","ate","nat","bat"]
Output: [["bat"],["nat","tan"],["ate","eat","tea"]]
Example 2:

Input: strs = [""]
Output: [[""]]
Example 3:

Input: strs = ["a"]
Output: [["a"]]
 

Constraints:

1 <= strs.length <= 104
0 <= strs[i].length <= 100
strs[i] consists of lowercase English letters.


```

class Solution(object):
    def groupAnagrams(self, strs):
        ans = collections.defaultdict(list)
        for s in strs:
            ans[tuple(sorted(s))].append(s)
        return ans.values()

```

Time Complexity: O(NKlog⁡K)O(NK \log K)O(NKlogK), where NNN is the length of strs, and KKK is the maximum length of a string in strs. The outer loop has complexity O(N)O(N)O(N) as we iterate through each string. Then, we sort each string in O(Klog⁡K)O(K \log K)O(KlogK) time.

Space Complexity: O(NK)O(NK)O(NK), the total information content stored in ans.

```

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dx =  defaultdict(list)
        for word in strs:
            count = [0]*26
            for c in word:
                count[ord(c)-97] += 1
            dx[tuple(count)].append(word)
        return dx.values()


```

Time Complexity: O(NK)O(NK)O(NK), where NNN is the length of strs, and KKK is the maximum length of a string in strs. Counting each string is linear in the size of the string, and we count every string.

Space Complexity: O(NK)O(NK)O(NK), the total information content stored in ans.
