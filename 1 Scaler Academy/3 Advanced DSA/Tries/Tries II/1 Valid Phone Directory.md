### Check of phone directory is Valid or not


Problem Description

Given a phone directory in the form of string array A containing N numeric strings.

If any phone number is prefix of another phone number then phone directory is invalid else it is valid.

You need to check whether the given phone directory is valid or not if it is valid then return 1 else return 0.



Problem Constraints

2 <= N <= 105

1 <= |A[i]| <= 50

A[i] consists only of numeric digits.



Input Format

First and only argument is an string array A.



Output Format

Return 1 if the given phone directory is valid else return 0.



Example Input

Input 1:

 A = ["1234", "2342", "567"]
Input 2:

 A = ["00121", "001"]


Example Output

Output 1:

 1
Output 2:

 0


Example Explanation

Explanation 1:

 No number is prefix of any other number so phone directory is valid so we will return 1.
Explanation 2:

 "001" is prefix of "00121" so phone directory is invalid so we will return 0.
 
 
 ```
 
 class TrieNode:

    def __init__(self,val):
        self.val = val;
        self.children = [None]*10;
        self.IsEnd = False;

class Trie:

    def __init__(self):

        self.root = TrieNode('#');
    
    def insertion(self,word):

        curr = self.root;
        size = len(word);

        for i in range(size):

            index = int(word[i]);

            if curr.children[index] == None:
                curr.children[index] = TrieNode(word[i]);
            
            curr = curr.children[index];
        
        curr.IsEnd = True;
    
    def search(self,word):

        curr = self.root;
        size = len(word);

        for i in range(size):

            index = int(word[i]);
            if curr.IsEnd == True:
                return 0;

            if curr.children[index] == None:
                return 1;


            curr = curr.children[index];
        return 0 if curr.IsEnd == True else 1;

class Solution:

    def solve(self, A):

        Trie_obj = Trie();
        A.sort();
        for phone_dir in A:
            if  Trie_obj.search(phone_dir) == 0:
                return 0;
            Trie_obj.insertion(phone_dir);
        return 1;
 
 ```
