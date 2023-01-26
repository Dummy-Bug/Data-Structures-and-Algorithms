### Problem Description

Given a sorted array of integers (not necessarily distinct) A and an integer B, find and return how many pair of integers ( A[i], A[j] ) 
such that i != j have sum equal to B.

Since the number of such pairs can be very large, return number of such pairs modulo (109 + 7).

Problem Constraints
1 <= |A| <= 100000

1 <= A[i] <= 10^9

1 <= B <= 10^9



Input Format
The first argument given is the integer array A.

The second argument given is integer B.



Output Format
Return the number of pairs for which sum is equal to B modulo (10^9+7).



Example Input
Input 1:

A = [1, 1, 1]
B = 2
Input 2:

 
A = [1, 1]
B = 2


Example Output
Output 1:

 3
Output 2:

 1


Example Explanation
Explanation 1:

 Any two pairs sum up to 2.
Explanation 2:

 only pair (1, 2) sums up to 2.

**Solution Approach**

Let us formulate a two pointer approach to the this problem.
We will first sort the given array and use two pointers i and j with i = 0, j = Length of Array - 1.
We will have three conditions:

1. A[i] + A[j] < sum  --> We will increase the pointer i.
2. A[i] + A[j] > sum  --> We will decrease the pointer j.
3. A[i] + A[j] = sum  --> We will count the frequency of A[i] and A[j] and multiply them and add to the answer.
Note, that if A[i] and A[j] are equal in value, then we will have to change the formula instead:
freq(A[i]) * freq(A[i]) –> freq(A[i]) * (freq(A[i]) - 1) / 2
to avoid overcounting pairs.

```

public class Solution {
    public int solve(int[] A, int B) {

        int p1 = 0; int p2 = A.length-1;
        long result = 0; int mod = 1000000000+7;

        while (p1 < p2){
            int x = A[p1]; 
            int y = A[p2];
            int sum = x+y;

            // System.out.println(x+y);
            if (sum>B){
                p2--;
            }
            else if(sum<B){
                p1++;
            }
            else{
                // System.out.println(x+" "+y);
                if (x==y){
                    long n = p2-p1+1;
                    result = ( (result)%mod + ( ( n*(n-1) )/2)%mod )%mod ;
                    return (int)result ;
                }
                long left_count  = 0;
                long right_count = 0;

                while(A[p1] == x){
                    left_count++;
                    p1++;
                }
                while(A[p2] == y){
                    right_count++;
                    p2--;
                }
                // System.out.println(left_count+" "+right_count);
                result = ( (result)%mod + (left_count*right_count)%mod )%mod;
            }
        }
        return (int)result;

    }
}


```
