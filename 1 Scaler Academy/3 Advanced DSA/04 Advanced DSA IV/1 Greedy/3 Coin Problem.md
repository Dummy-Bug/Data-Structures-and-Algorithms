### Problem Description

The monetary system in DarkLand is really simple and systematic. The locals-only use coins. The coins come in different values. The values used are:

 1, 5, 25, 125, 625, 3125, 15625, ...
Formally, for each K >= 0 there are coins worth 5K.

Given an integer A denoting the cost of an item, find and return the smallest number of coins necessary to pay exactly the cost of the item (assuming you have a sufficient supply of coins of each of the types you will need).



Problem Constraints
1 <= A <= 2×109



Input Format
The only argument given is integer A.



Output Format
Return the smallest number of coins necessary to pay exactly the cost of the item.



Example Input
Input 1:

 A = 47
Input 2:

 A = 9


Example Output
Output 1:

 7
Output 2:

 5


Example Explanation
Explanation 1:

 Representation of 7 coins will be : (1 + 1 + 5 + 5 + 5 + 5 + 25).
Explanation 2:

 Representation of 5 coins will be : (1 + 1 + 1 + 1 + 5).
 
 
 
 **Solution Approach**
 
We will use the Greedy solution.

Start from the largest possible denomination and keep adding denominations while the remaining value is greater than 0.

The number of the chosen coin is determined by the A/(coin value).
 
 
 ```
 
import math
class Solution:

    def solve(self, curr_cost):
        
        if curr_cost<5:
            return curr_cost;

        i = 1; curr_coin = 5;
        while curr_coin <= curr_cost:
            curr_coin = curr_coin*5;
        
        curr_coin = curr_coin//5;

        total_coins = 0;

        while curr_coin != 0:

            total_coins = total_coins + curr_cost//curr_coin;
            curr_cost = curr_cost%curr_coin;
            curr_coin = curr_coin//5;
        
        return total_coins;
 
 
 ```
