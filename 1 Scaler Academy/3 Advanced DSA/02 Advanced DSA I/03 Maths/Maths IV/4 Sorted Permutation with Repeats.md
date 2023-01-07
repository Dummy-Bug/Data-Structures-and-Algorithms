### Problem Description

Given a string A, find the rank of the string amongst its permutations sorted lexicographically. Note that the characters might be repeated. If the characters are repeated, we need to look at the rank in unique permutations. Look at the example for more details.

NOTE:

The answer might not fit in an integer, so return your answer % 1000003 where 1000003 is a prime number.
String A can consist of both lowercase and uppercase letters. Characters with lesser ASCII values are considered smaller, i.e., 'a' > 'Z'.


Problem Constraints
1 <= len(A) <= 1000000



Input Format
First argument is a string A.



Output Format
Return an integer denoting the rank.



Example Input
Input 1:

 A = "aba"
Input 2:

 A = "bca"


Example Output
Output 1:

 2
Output 2:

 4


Example Explanation
Explanation 1:

 The order permutations with letters 'a', 'a', and 'b' :
    aab
    aba 
    baa
 So, the rank is 2.
Explanation 2:

 The order permutations with letters 'a', 'b', and 'c' :
    abc
    acb 
    bac
    bca
    cab
    cba
 So, the rank is 4
 
 **Approach**
 
 Let’s start by looking at the first character.

If the first character is X, all permutations which had the first character less than X would come before this permutation 
when sorted lexicographically.

The number of permutations with a character C as the first character = number of permutations possible with remaining 
N-1 character = (N-1)! / (p1! * p2! * p3! ... ) where p1, p2, p3 are the number of occurrences of repeated characters.

For example, number of permutations possible with 3 ‘a’ and 3 ‘b’ is 6! / 3! 3! = 20

Hence,

rank = number of permutations possible with placing characters smaller than the current first character in the first position + rank of 
permutation of the string with the first character removed
So, we take a loop on the possibilities for the first character, and if that character is less than the current first character, 
we calculate the number of permutations using the formula given above (N-1)! / (p1! * p2! * p3! ... )

Now, there is a slight problem.
(N-1)! / (p1! * p2! * p3! ... ) does not necessarily fit in an integer. It is easy to calculate (N-1)! % MOD.
However, how do we handle divisions? Modular_multiplicative_inverse is what you are looking for.
In short,

(1/A) % MOD = A ^ (MOD - 2) % MOD
 
 
 **Notes**
 --> To be Done:-
 ```
 
 MOD = 1000003

def initializeFactorials( totalLen, fact):
    # calculates factorial
    factorial = 1
    fact.append(1) # 0 != 1
    for curIndex in range(1,totalLen):
        factorial = (factorial * curIndex) % MOD
        fact.append(factorial)

def inverseNumber( num):
    # Find the modular multiplicative inverse
    # Calculates (num ^ (MOD - 2)) % MOD
    ans = 1
    base = num
    power = MOD - 2
    while (power > 0):
        if (power == 1):
            return (ans * base) % MOD
        
        if (power % 2 == 0):
            base = (base * base) % MOD
            power = power // 2
        else:
            ans = (ans * base) % MOD
            power -= 1
    return ans

class Solution:
	# @param A : string
	# @return an integer
	def findRank(self, A):
        # Initializations
        charCount = [0] * 256 # count of characters in A. 
        
        for i in range(len(A)):
            charCount[ord(A[i])] += 1
        
        fact = [] # fact[i] will contain i! % MOD
        
        initializeFactorials(len(A) + 1, fact)
    
        rank = 1
        for i in range(len(A)):
            # find number of permutations placing character smaller than A[i] at ith position 
            # among characters from i to A.length 
            less = 0
            remaining = len(A) - i - 1
            for ch in range(ord(A[i])):
                if (charCount[ch] == 0):
                    continue
                # Lets try placing ch as the first character in remaining characters
                # and check the number of permutation possible.
                charCount[ch] -= 1
                numPermutation = fact[remaining]
            
                for c in range(128):
                    if (charCount[c] <= 1):
                        continue 
                    numPermutation = (numPermutation * inverseNumber(fact[charCount[c]])) % MOD
                
                charCount[ch] += 1
                less = (less + numPermutation) % MOD
            
            rank = (rank + less) % MOD
            # remove the current character from the set. 
            charCount[ord(A[i])] -= 1
        return rank
 
 ```
