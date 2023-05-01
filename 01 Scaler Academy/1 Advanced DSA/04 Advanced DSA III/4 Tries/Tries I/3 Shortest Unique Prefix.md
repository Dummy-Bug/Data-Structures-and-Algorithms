### Shortest Unique Prefix

https://www.interviewbit.com/problems/shortest-unique-prefix/



**Solution Approach**

-> Lets take an example:

input: ["zebra", "dog", "duck", "dot"]

Now we will build prefix tree and we will also store count of characters

                root
                /|
         (d, 3)/ |(z, 1)
              /  |
          Node1  Node2
           /|        \
     (o,2)/ |(u,1)    \(e,1)
         /  |          \
   Node1.1  Node1.2     Node2.1
      | \         \            \
(g,1) |  \ (t,1)   \(c,1)       \(b,1)
      |   \         \            \ 
    Leaf Leaf       Node1.2.1     Node2.1.1
    (dog)  (dot)        \                  \
                         \(k, 1)            \(r, 1)
                          \                  \   
                          Leaf               Node2.1.1.1
                          (duck)                       \
                                                        \(a,1)
                                                         \
                                                         Leaf
                                                         (zebra)

Now, for every leaf / word , we find the character nearest to the root with frequency as 1. 
The prefix that the path from root to this character corresponds to, is the representation of the word. 

```

class TrieNode():

    def __init__(self,data):

        self.data = data;
        self.children   = [None]*26;
        self.isEnd      = False;
        self.freq_count = 0;
     
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
            curr.freq_count += 1;
        
        curr.isEnd = True;

    def shortextPrefix(self,word):
        prefix = '';

        curr = self.root;
        size = len(word);

        for i in range(size):
            index = ord(word[i]) - ord('a');
            prefix = prefix + word[i];
            if curr.children[index].freq_count == 1:
                return prefix;
            curr = curr.children[index];
        
        return prefix;

class Solution:

	def prefix(self, A):

        Trie_object = Trie();
        result = [];

        for word in A:
            Trie_object.insert(word);
        
        for word in A:
            result.append(Trie_object.shortextPrefix(word));
        
        return result;




```
