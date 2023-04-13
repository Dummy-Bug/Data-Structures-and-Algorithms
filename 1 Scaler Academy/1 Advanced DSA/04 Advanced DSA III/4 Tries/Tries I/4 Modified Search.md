### Modified Search

Problem Description

Given two arrays of strings A of size N and B of size M.

Return a binary string C where C[i] = '1' if B[i] can be found in dictionary A using exactly one modification in B[i], Else C[i] = '0'.

NOTE: modification is defined as converting a character into another character.



Problem Constraints

1 <= N <= 30000

1 <= M <= 2500

1 <= length of any string either in A or B <= 20

strings contains only lowercase alphabets



Input Format

First argument is the string arrray A.

Second argument is the string array B.



Output Format

Return a binary string C where C[i] = '1' if B[i] can be found in dictionary A using one modification in B[i], Else C[i] = '0'.



Example Input

Input 1:

 A = [data, circle, cricket]
 B = [date, circel, crikket, data, circl]
Input 2:

 A = [hello, world]
 B = [hella, pello, pella]


Example Output

Output 1:

 "10100"
Output 2:

 "110"


Example Explanation

Explanation 1:

 1. date = dat*(can be found in A)
 2. circel =(cannot be found in A using exactly one modification)
 3. crikket = cri*ket(can be found in A)
 4. data = (cannot be found in A using exactly one modification)
 5. circl = (cannot be found in A using exactly one modification)
Explanation 2:

 Only pella cannot be found in A using only one modification.
 
 
 
 ```
 
 class TrieNode():

    def __init__(self,data):

        self.data = data;
        self.children   = [None]*26;
        self.isEnd      = False;
     
class Trie():

    def __init__(self):

        self.root = TrieNode('#');

    def insert(self,word):

        curr = self.root;
        size = len(word);

        for i in range(size):
            index = ord(word[i]) - ord('a');

            if curr.children[index] == None:
                curr.children[index] = TrieNode(word[i]);

            curr = curr.children[index];
        
        curr.isEnd = True;


    def searching(self,word):
        # print(word);
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

        Trie_object = Trie();
        result = [];

        for word in A:
            Trie_object.insert(word);
        
        for word in B:
            Match = False;

            for i in range(len(word)):
                for j in range(ord('a'),ord('z')+1):

                    if chr(j) == word[i]:
                        continue;

                    if i == len(word)-1 and len(word)>1:
                        
                        if Trie_object.searching(word[0:len(word)-1]+chr(j)):
                            Match = True;
                            break;

                    elif i == 0 and len(word)>1:

                        if Trie_object.searching(chr(j)+word[1:]):
                            Match = True;
                            break;
                    
                    elif len(word)== 1:
                        if Trie_object.searching(chr(j)):
                            rMatch = True;
                            break;
                    else:
                        if Trie_object.searching(word[0:i]+chr(j)+word[i+1:]):
                            Match = True;
                            break;
                if Match == True:
                    result.append('1');
                    break;
            else:
                result.append('0');
            # print(result)
                
        return "".join(result);
 
 ```
