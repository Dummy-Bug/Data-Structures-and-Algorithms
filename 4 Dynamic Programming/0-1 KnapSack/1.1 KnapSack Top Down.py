https://practice.geeksforgeeks.org/problems/0-1-knapsack-problem0945/1#

class Solution:
    
    def funcn(self,capacity,wt_array,val_array,n):
        
        if n <= 0:
            return 0
            
        if self.dp[n][capacity] != -1:
            return self.dp[n][capacity]
            
        if wt_array[n-1] <= capacity: # if value's weight is lesser then we have two choices.
        
            value_considered = val_array[n-1] + self.funcn(capacity - wt_array[n-1],wt_array,val_array,n-1)
                            #  calling the function with new capacity and new size of the array
        
            not_considered   = 0 + self.funcn(capacity,wt_array,val_array,n-1)
                            # if not considered then just decrease the size of the array.  
                            
            self.dp[n][capacity] = max(value_considered,not_considered)
            return self.dp[n][capacity]
            
        else:
            
            return self.funcn(capacity,wt_array,val_array,n-1)
    
    def knapSack(self,W, wt, val, n):
        
        #  https://www.geeksforgeeks.org/python-using-2d-arrays-lists-the-right-way/
        
        self.dp = [[ -1 for i in range( 0,W+1)]for j in range( 0,n+1 )] # +1 so that we can have value of dp[val][w]
        # 2D array because two variables are changing in our recursive function.
        # only take the variables that are changing ignore the rest of the variables for dp array.
        
        return self.funcn(W,wt,val,n)