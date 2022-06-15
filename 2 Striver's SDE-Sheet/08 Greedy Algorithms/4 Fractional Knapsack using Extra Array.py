# https://practice.geeksforgeeks.org/problems/fractional-knapsack-1587115620/1#
'''
Time Complexity: O(n log n + n). O(n log n) to sort the items and O(n) to iterate through all the items for calculating the answer.

Space Complexity: O(n), as we used an extra Array
'''
class Solution:    
    
    def fractionalknapsack(self, W,Items,n):
        
        array = []
        max_profit = 0.0
        
        for i in range(n):
            value  = Items[i].value
            weight = Items[i].weight
            
            array.append([value,weight,value/weight])
        
        array.sort(reverse = True,key = lambda x:x[2])
        # print(array)
        for i in range(n):
            
            if W - array[i][1]  >= 0:
                max_profit = max_profit + array[i][0]
                W = W-array[i][1]
            
            else:
                max_profit = max_profit + float(W)*array[i][2]
                break

        return max_profit