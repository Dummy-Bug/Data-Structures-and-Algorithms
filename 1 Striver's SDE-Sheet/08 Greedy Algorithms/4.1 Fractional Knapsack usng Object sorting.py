# https://practice.geeksforgeeks.org/problems/fractional-knapsack-1587115620/1#
'''
Time Complexity: O(n log n + n). O(n log n) to sort the items and O(n) to iterate through all the items for calculating the answer.

Space Complexity: O(1), as sorted the object itself
'''
class Solution:    
    
    def fractionalknapsack(self, W,Items,n):
        
        items = sorted(Items,key = lambda x:(x.value/x.weight),reverse = True)
        max_profit = 0.0
        
        for i in range(len(items)):
            
            value ,weight = items[i].value,items[i].weight
            
            if W - weight  >= 0:
                max_profit = max_profit + value
                W = W-weight
            
            else:
                max_profit = max_profit + float(W)*value/weight
                break

        return max_profit