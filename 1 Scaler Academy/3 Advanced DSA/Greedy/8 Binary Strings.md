Problem Description
You are given a string A consisting of 1's and 0's. Now the task is to make the string consisting of only 1's. But you are allowed to perform only the following operation:

Take exactly B consecutive string elements and change 1 to 0 and 0 to 1.
Each operation takes 1 unit time, so you have to determine the minimum time required to only make the string of 1's. If not possible, return -1.



Problem Constraints
2 ≤ length of A ≤ 105
2 ≤ B ≤ (length of A)



Input Format
The first argument is a string A consisting of 1's and 0's.
The second argument is an integer B which represents the number of consecutive elements which can be changed.



Output Format
Return an integer which is the minimum time to make the string of 1's only or -1 if not possible.



Example Input
Input 1:

 A = "00010110"
 B = 3
Input 2:

 A = "011"
 B = 3


Example Output
Output 1:

 3
Output 2:

 -1


Example Explanation
Explanation 1:

 You can get 1 by first changing the leftmost 3 elements, getting to 11110110, then the rightmost 3, getting to 11110001, 
 and finally the 3 left out 0's to 11111111; In 3 unit time.
Explanation 2:

It's not possible to convert the string into string of all 1's.


**Approach 1*

```
TC - O(n * B), SC - O(1) , TLE

Iterate from starting whenever A[i] == '0' , flip all the next B bits. Continue the iteration from i + 1.

public int solve(String A, int B) {
        char[] aCharArr = A.toCharArray();
        int steps = 0;
        for(int i = 0; i < A.length(); i++){
            if(aCharArr[i] == '0' && i + B <= A.length()){
                steps++;
                for(int j = i; j < i + B; j++){
                    if(aCharArr[j] == '0'){
                        aCharArr[j] = '1';
                    } else {
                        aCharArr[j] = '0';
                    }
                }
            }
            if(i + B > A.length()){
                break;
            }
        }
        for(int i = 0; i < A.length(); i++){
            if(aCharArr[i] == '0'){
                return -1;
            }
        }
        return steps;

    }
    
```

**optimal Approach**

```

class Solution:

    def solve(self, A, B):

        xor = 0; num_flips = 0;
        flipBits = [0]*len(A);

        # xor = 1 means a flip is in progress.
        for i in range(len(A)-B+1):

            xor = xor ^ flipBits[i];

            if (xor == 0 and A[i] == '0' )or(xor == 1 and A[i] == '1'):
                xor = xor^1 # flip the xor;
                num_flips += 1;

                if i+B<len(A):
                    flipBits[i+B] = 1;
        
        for i in range(len(A)-B+1,len(A)):
            xor = xor^flipBits[i];
            if (A[i] == '0' and xor == 0) or (A[i] == '1' and xor == 1):
                return -1;
        return num_flips


```
