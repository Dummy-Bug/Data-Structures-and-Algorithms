**Problem Description**

There are A beggars sitting in a row outside a temple. Each beggar initially has an empty pot. When the devotees come to the temple, they donate some amount of coins to these beggars. Each devotee gives a fixed amount of coin(according to their faith and ability) to some K beggars sitting next to each other.

Given the amount P donated by each devotee to the beggars ranging from L to R index, where 1 <= L <= R <= A, find out the final amount of money in each beggar's pot at the end of the day, provided they don't fill their pots by any other means.
For ith devotee B[i][0] = L, B[i][1] = R, B[i][2] = P, Given by the 2D array B


**Problem Constraints**

1 <= A <= 2 * 105
1 <= L <= R <= A
1 <= P <= 103
0 <= len(B) <= 105


**Input Format**

The first argument is a single integer A.
The second argument is a 2D integer array B.


**Output Format**

Return an array(0 based indexing) that stores the total number of coins in each beggars pot.


Example Input
Input 1:-

A = 5

B = [[1, 2, 10], [2, 3, 20], [2, 5, 25]]


Example Output

Output 1:-

10 55 45 25 25


**Example Explanation**

Explanation 1:-
First devotee donated 10 coins to beggars ranging from 1 to 2. Final amount in each beggars pot after first devotee: [10, 10, 0, 0, 0]
Second devotee donated 20 coins to beggars ranging from 2 to 3. Final amount in each beggars pot after second devotee: [10, 30, 20, 0, 0]
Third devotee donated 25 coins to beggars ranging from 2 to 5. Final amount in each beggars pot after third devotee: [10, 55, 45, 25, 25]


**Naive Approach**

The simple naive solution would be to iterate over each devotee and add their donation to each beggar’s pot. You need to iterate through each beggar’s pot from i to j range donated by each devotee.

The worst time complexity of the above approach is O(D*R), where D is the total number of devotees and R is the maximum range of beggars index.

<hr> 

***NOTES***

> Instead of updating each beggar ranging from i to j, we could update index i with +S and index j + 1 with -S, where S is a donation made by some devotee. So if you want to know the number of coins taken by kth beggar, you just need to find the prefix sum of all the values(coins) from 1 to k(Try to prove it by yourself that values between i to j contains +S as you are doing prefix sum).

> **This technique is known as difference array and is very helpful in problems which involves range updates.**

Time complexity : O(A+n) , where n denotes the size of B

Space complexity : O(A)

Example:

N = 5, D = [[1, 2, 10], [2, 3, 20], [2, 5, 25]]

Initial Coin array: [0, 0, 0, 0, 0]

* After first devotee, if we update i = 1 with +10 and j + 1 = 3 with -10, we get [10, 0, -10, 0, 0]. Now note that if you add 10 to 1st index and subtract 10 with 3rd index and do a prefix sum at every array element, you will get +10 at 1st and 2nd.

* After second devotee, if we update i = 2 with +20 and j + 1 = 4 with -20, we get [10, 20, -10, -20, 0].

* Similarly, after third devotee, if we update i = 2 with +25 and j + 1 = 6 with -25, we get [10, 45, -10, -20, 0].
Now, if we calculate the prefix sum at every index, we get [10, 55, 45, 25, 25].



```
class Solution:
    def solve(self, A, B):

        coins = [0]*A 

        for i in range(len(B)):

            start_index  = B[i][0] - 1
            end_index    = B[i][1] - 1

            donation     = B[i][2]

            coins[start_index] = coins[start_index]  + donation

            if end_index + 1 < len(coins):

                coins[end_index+1] = coins[end_index+1] - donation
        
        for i in range(1,A):

            coins[i] = coins[i] + coins[i-1]
        
        return coins

```
