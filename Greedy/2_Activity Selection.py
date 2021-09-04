class Solution:
    def activitySelection(self,n,start,end):
       
        arr = []
        
        for i in range(n):
            arr.append([start[i],end[i]])
        arr = sorted(arr,key = lambda x: x[1])
        
        end_time = 0
        count    = 0
        
        for i in range(n):
            
            if end_time >= arr[i][0]:
                continue
            
            count = count + 1
            end_time = arr[i][1]
            
        return count