### Spelling Checker 

Q1. Spelling Checker
Solved
character backgroundcharacter
Stuck somewhere?
Ask for help from a TA and get it resolved.
Get help from TA.
Problem Description
Given an array of words A (dictionary) and another array B (which contain some words).

You have to return the binary array (of length |B|) as the answer where 1 denotes that the word is present in the dictionary and 0 denotes it is not present.

Formally, for each word in B, you need to return 1 if it is present in Dictionary and 0 if not.

Such problems can be seen in real life when we work on any online editor (like Google Documnet), if the word is not valid it is underlined by a red line.

NOTE: Try to do this in O(n) time complexity.



Problem Constraints
1 <= |A| <= 1000

1 <= sum of all strings in A <= 50000

1 <= |B| <= 1000



Input Format
First argument is array of strings A.

First argument is array of strings B.



Output Format
Return the binary array of integers according to the given format.



Example Input
Input 1:

A = [ "hat", "cat", "rat" ]
B = [ "cat", "ball" ]
Input 2:

A = [ "tape", "bcci" ]
B = [ "table", "cci" ]


Example Output
Output 1:

[1, 0]
Output 2:

[0, 0]


Example Explanation
Explanation 1:

Only "cat" is present in the dictionary.
Explanation 2:

None of the words are present in the dictionary.



**Approach 1**

-> Using HashSet

```

class Solution:
    def solve(self, A, B):

        Hash_set = set();

        for word in A:
            Hash_set.add(word);

        result = [];

        for word in B:
            if word in Hash_set:
                result.append(1);
            else:
                result.append(0);
        return result;


```

**Using Tries**

```

class TrieNode:

    def __init__(self):
        self.children = [None]*26;
        self.isEnd    = False;

class Trie:

    def __init__(self):
        self.root = TrieNode();

    def insertion(self,word):

        curr = self.root;
        size = len(word);

        for i in range(size):
            index = ord(word[i]) - ord('a');

            if curr.children[index] == None:
                curr.children[index] = TrieNode();
            
            curr = curr.children[index];
        
        curr.isEnd = True;

    def searching(self,word):

        curr = self.root;
        size = len(word);

        for i in range(size):
            index = ord(word[i]) - ord('a');

            if curr.children[index] == None:
                return 0;
            
            curr = curr.children[index];
        
        return 1 if curr.isEnd else 0;




class Solution:
    def solve(self, A, B):

        Trie_obj = Trie();

        for word in A:
            Trie_obj.insertion(word);
        
        result = [];
        for word in B:
            result.append(Trie_obj.searching(word));
        
        return result;



```
