### Problem Description

Rishabh was sitting ideally in his office and then suddenly his boss gave him some operations to perform.

You being his friend tried to help him in finishing the task fast.

So you have to perform Q operation of two types:

Operation 1: INSERT : You are given an pair of (string, integer).The string represents the key and the integer represents the value. 
Insert the key-value pair in the hash and If the key already exists in hash, then the original key-value pair will be overridden to the new one.
Operation 2: SUM : you'll be given an pair of (string, -1) where string representing the prefix, and you need to return the sum of all the pairs'
value in the hash whose key starts with the prefix.


Problem Constraints

1 <= Q <= 103

1 <= Length of string in any operation <= 30

Strings in each operations only consists of lowercase characters.

1 <= Integer in Operation 1 <= 100

Integer in operation 2 is always -1 so this parameter will help you in distinguishing between the two opearations.



Input Format

First argument is an string array A of size Q denoting the first parameter of each operations.

Seond argument is an integer array B of size Q denoting the second parameter of each operations.

NOTE: ith query will be like (A[i], B[i])



Output Format

Return an integer array denoting the answer for each operation of type: 2



Example Input

Input 1:

 A = ["apple", "ap", "app", "ap"]
 B = [3, -1, 2, -1]
Input 2:

 A = ["ban", "banana", "ba"]
 B = [10, -1, -1]


Example Output

Output 1:

 [3, 5]
Output 2:

 [0, 10]


Example Explanation

Explanation 1:

 1. (A[0], B[0]) is a type-1 operation as B[0] != -1 so we will insert "apple" in our hash and store its value as 3.
 2. (A[1], B[1]) is a type-2 operation as B[1] == -1 so we will search for every string inserted in our 
    hash whose prefix is  "ap". Only "apple" has its prefix as "ap" so we will return 3
 3. (A[2], B[2]) is a type-1 operation as B[2] != -1 so we will insert "app" in our hash and store its value as 2.
 4. (A[3], B[3]) is a type-2 operation as B[3] == -1 so we will search for every string inserted in our 
    hash whose prefix is  "ap". So both ["apple", "app"] has its prefix as "ap" so we will return 3 + 2 i.e 5
Explanation 2:

 1. (A[0], B[0]) is a type-1 operation as B[0] != -1 so we will insert "ban" in our hash and store its value as 10.
 2. (A[1], B[1]) is a type-2 operation as B[1] == -1 so we will search for every string inserted in our 
    hash whose prefix is  "banana". So there doesn't exist any string whose prefix is "banana" so we will return 0
 3. (A[2], B[2]) is a type-2 operation as B[2] == -1 so we will search for every string inserted in our 
    hash whose prefix is  "ba". Only "ban" has its prefix as "ba" so we will return 10.
    
    
    **Approach**
    
    Approach #1: Brute Force [Accepted]

Intuition and Algorithm:

For each key in the map, if that key starts with the given prefix, then add it to the answer.
Complexity Analysis
Time Complexity: Every insert operation is O(1). Every sum operation is O(N * P) where N is the number of items in the map, and P is the length of the input prefix.

Space Complexity: The space used by map is linear in the size of all input key and val values combined.


Approach #2: Prefix Hashmap [Accepted]

Intuition and Algorithm:

We can remember the answer for all possible prefixes in a HashMap score. When we get a new (key, val) pair, we update every prefix of key appropriately: each prefix will be changed by delta = val - map[key], where map is the previous associated value of key (zero if undefined.)

Complexity Analysis

Time Complexity: Every insert operation is O(K2) where K is the length of the key, as K strings are made of an average length of K. Every sum operation is O(1).

Space Complexity: The space used by map is linear in the size of all input key and val values combined.


Approach #3: Trie [Accepted]

Intuition and Algorithm:

Since we are dealing with prefixes, a Trie (prefix tree) is a natural data structure to approach this problem. For every node of the trie corresponding to some prefix, we will remember the desired answer (score) and store it at this node. As in Approach #2, this involves modifying each node by delta = val - map[key].
Complexity Analysis
Time Complexity: Every insert operation is O(K), where K is the length of the key. Every sum operation is O(K).

Space Complexity: The space used is linear in the size of the total input.



```

class TrieNode:
    def __init__(self,total_sum = 0):
        self.edges = {}
        self.total_sum = 0

class Trie:
    def __init__(self):
        self.root = TrieNode()
        self.keys = {}

    def insert(self,word: str,val: int):
        cur_node = self.root
        diff     = self.keys.get(word,0)      # get for duplicate key present in dict 
        diff     = val - diff
        self.keys[word] = val
        cur_node.total_sum += diff 

        for char in word:
            if char not in cur_node.edges:
                cur_node.edges[char] = TrieNode()
            cur_node = cur_node.edges[char]
            cur_node.total_sum += diff

    def getprefixSum(self,prefix: str) -> int:
        cur_node = self.root
        for char in prefix:
            if char not in cur_node.edges:
                return 0
            cur_node = cur_node.edges[char]
        return cur_node.total_sum

class Solution:
    def solve(self, A, B):
        ans = []

        N = len(A)
        trie = Trie()
        for i in range(N):
            if B[i] == -1:
                ans.append(trie.getprefixSum(A[i]))
            else:
                trie.insert(A[i],B[i])

        return ans 
        
```
