### Problem Description

Given a string A denoting a stream of lowercase alphabets, you have to make a new string B.
B is formed such that we have to find the first non-repeating character each time a character is inserted to the stream and append it at 
the end to B. If no non-repeating character is found, append '#' at the end of B.



Problem Constraints
1 <= |A| <= 100000



Input Format
The only argument given is string A.



Output Format
Return a string B after processing the stream of lowercase alphabets A.



Example Input
Input 1:

 A = "abadbc"
Input 2:

 A = "abcabc"


Example Output
Output 1:

"aabbdd"
Output 2:

"aaabc#"


Example Explanation
Explanation 1:

"a"      -   first non repeating character 'a'
"ab"     -   first non repeating character 'a'
"aba"    -   first non repeating character 'b'
"abad"   -   first non repeating character 'b'
"abadb"  -   first non repeating character 'd'
"abadbc" -   first non repeating character 'd'
Explanation 2:

"a"      -   first non repeating character 'a'
"ab"     -   first non repeating character 'a'
"abc"    -   first non repeating character 'a'
"abca"   -   first non repeating character 'b'
"abcab"  -   first non repeating character 'c'
"abcabc" -   no non repeating character so '#'

**Approach**

You need to maintain a map for each character of the stream.
After that, you can also maintain a queue for the extraction of information.
Each character is inserted and removed from the queue at most once; hence time complexity is O(n).
Code looks something like
for (auto c : A)
{
mp[c]++;
q.push(c);
while (!q.empty() && mp[q.front()] > 1) q.pop();
if (!q.empty()) ans.push_back(q.front());
else ans.push_back(‘#’);
}


```

from collections import deque;

class Solution:

    def solve(self, A):

        Hash_Map = dict();
        q = deque(); result = '';

        for char in A:

            if char not in Hash_Map:
                Hash_Map[char] = 0;
            Hash_Map[char] += 1;

            if Hash_Map[char] == 1:
                q.append(char);

            if len(q) != 0 :
                if Hash_Map[q[0]] < 2:
                    result += q[0];
                else:
                    while len(q) != 0 and Hash_Map[q[0]] > 1:
                        q.popleft();
                    if len(q) != 0:
                        result += q[0];

            if len(q) == 0:
                    result += '#';
                    
        return result;


```
