### Problem Description

Given an array, A of integers of size N. Find the subarray AL, AL+1, AL+2, ... AR with 1<=L<=R<=N, which has maximum XOR value.

NOTE: If there are multiple subarrays with the same maximum value, return the subarray with minimum length. If the length is the same, 
return the subarray with the minimum starting index.



Problem Constraints
1 <= N <= 100000
0 <= A[i] <= 109



Input Format
First and only argument is an integer array A.



Output Format
Return an integer array B of size 2. B[0] is the starting index(1-based) of the subarray and B[1] is the ending index(1-based) of the subarray.



Example Input
Input 1:

 A = [1, 4, 3]
Input 2:

 A = [8]


Example Output
Output 1:

 [2, 3]
Output 2:

 [1, 1]


Example Explanation
Explanation 1:

 There are 6 possible subarrays of A:
 subarray            XOR value
 [1]                     1
 [4]                     4
 [3]                     3
 [1, 4]                  5 (1^4)
 [4, 3]                  7 (4^3)
 [1, 4, 3]               6 (1^4^3)

 [4, 3] subarray has maximum XOR value. So, return [2, 3].
Explanation 2:

 There is only one element in the array. So, the maximum XOR value is equal to 8 and the only possible subarray is [1, 1]. 
 
 **Approach**
 
 Build a prefXor array in which the ith element represents the xor of all elements from 0 to i. To find the xor of any subarray[l..r], 
 we can just take the xor of prefXor[r] and prefXor[l-1].

To find the maximum xor subarray ending at the index i, insert the bit representation(starting from most significant bit) of all the 
elements of prefXor array upto i-1 into the trie data structure.
We have two possible cases at ith index.

The prefix itself has maximum xor.
We need to remove some prefix (ending at index from 0 to i-1).Try to have most significant bit to be set bit i.e. 1. As we have maintained 
the trie data structure of bit representation of i-1 elements of prefXor array, we can find the maximum xor in O(logm) where m is the maximum
number present in the given array.
We can find the maximum subarray ending at every index and return the subarray, which has the maximum XOR value.


```

class TrieNode:
    def __init__(self):
        self.children = [None]*2;
        self.end_pos  = None

class Trie:
    def __init__(self):
        self.root = TrieNode();
   
    def check_bit(self, num, bit_pos):
        return (num>>bit_pos) & 1
   
    def insert(self, num, msb_pos, end_pos):
        temp = self.root;

        for i in range(msb_pos, -1, -1):
            bit = self.check_bit(num, i)
            if temp.children[bit]:
                temp = temp.children[bit]
            else:
                temp.children[bit] = TrieNode()
                temp = temp.children[bit]
        temp.end_pos = end_pos
   
    def find_local_max(self, num, msb_pos, item_end_pos):
        temp = self.root
        ans = 0
        for i in range(msb_pos, -1, -1):
            bit = self.check_bit(num, i)
            required_bit = 1-bit
            if temp.children[required_bit]:
                ans += 1<<i
                temp = temp.children[required_bit]
            else:
                temp = temp.children[bit]
       
        maxi = max(temp.end_pos, item_end_pos)
        mini = min(temp.end_pos, item_end_pos)
        
        return ans, mini+1, maxi

class Solution:

    def solve(self, A):
        # make A as prefix xor
        ans = A[0]
        ans_start = 0
        ans_end = 0
        for i in range(1, len(A)):
            A[i] = A[i]^A[i-1];
            # check for subarrays xor starting with index 0;
            if A[i] > ans:
                ans = A[i]
                ans_start = 0
                ans_end = i
       
        trie = Trie();
        maxi = max(A);

        # find msb pos
        msb_pos = 0
        for i in range(31,-1,-1):
            if trie.check_bit(maxi, i):
                msb_pos = i
                break

        #print(msb_pos)
        for i in range(0, len(A)):
            trie.insert(A[i], msb_pos, i)
       
       
        for i in range(0, len(A)):
            local_max, start, end = trie.find_local_max(A[i], msb_pos, i)
            if local_max > ans:
                ans_start = start
                ans_end = end
                ans = local_max
            elif local_max == ans:
                if (end-start) < (ans_end-ans_start): # if subarrys size is not equal
                    ans_start = start
                    ans_end = end
                elif (end-start) == (ans_end-ans_start): # if subarrys size is equal
                    if start < ans_start:
                        ans_start = start
                        ans_end = end
        return [ans_start+1, ans_end+1]

```
