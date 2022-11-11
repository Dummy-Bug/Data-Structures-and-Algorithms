### Problem Description

A message containing letters from A-Z is being encoded to numbers using the following mapping:

'A' -> 1
'B' -> 2
...
'Z' -> 26
Given an encoded message denoted by string A containing digits, determine the total number of ways to decode it modulo 109 + 7.

https://leetcode.com/problems/decode-ways/submissions/517352846/


Lets first look at the bruteforce solution.
It only makes sense to look at 1 digit or 2 digit pairs ( as 3 digit sequence will be greater than 26 ).

So, when looking at the start of the string, we can either form a one digit code, and then look at the ways of forming the rest of the string of length L - 1, or we can form 2 digit code if its valid and add up the ways of decoding rest of the string of length L - 2.
This obviously is exponential.


```

import sys;
sys.setrecursionlimit(10**9);

class Solution:
    def numDecodings(self,s):
        array = [-1]*len(s)
        return self.rec(s,0,array)
        
    def rec(self,s,index,dp):
        mod = 10**9+7;
        if index >= len(s) :
            return 1
        if s[index] == "0":
            return 0
        if len(s) == index + 1:
            return 1 # if we have reached the end of the string then there's atleast one mapping possible.
        if dp[index] > -1:
            return dp[index]
        call_1 = self.rec(s,index+1,dp)
        call_2 = 0
        if int(s[index])*10 + int(s[index+1]) <= 26 :
            call_2 = self.rec(s,index+2,dp)
        dp[index] = (call_1 + call_2)%mod
        return dp[index]

```
