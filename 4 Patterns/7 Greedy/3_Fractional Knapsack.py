class Solution:
    def fractionalknapsack(self, W,Items,n):
        lst = []
        for i in range(len(Items)):
            val , wt = Items[i].value, Items[i].weight
            lst.append((val,wt,val*1.0/wt)) # use floating division here
            
        lst = sorted(lst,reverse=True,key=lambda x:x[2])
        result = 0
        for tup in lst:
            val, wt, profit = tup
            if W - wt >= 0:
                result = result + val
                W = W - wt
            else:
                result = result +  W *1.0/wt*val # unit factorization 
                break
        return result