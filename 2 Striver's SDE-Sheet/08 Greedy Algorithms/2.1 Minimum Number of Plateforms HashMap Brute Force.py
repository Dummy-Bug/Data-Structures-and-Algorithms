# https://practice.geeksforgeeks.org/problems/minimum-platforms-1587115620/1#
class Solution:    
    
    def minimumPlatform(self,n,arr,dep):

        
        aux_array = []
        
        for i in range(n):
            aux_array.append([arr[i],dep[i]])
        
        aux_array = sorted(aux_array,key = lambda x:x[0])
        # print(aux_array)
            
        plateforms = 1
        map =  dict()
        
        prev_departure_time = aux_array[0][1]
        map[plateforms] = prev_departure_time # store the latest departure time
        
        for i in range(1,n):
            
            current_arrival_time   = aux_array[i][0]
            current_departure_time = aux_array[i][1]
            
            for i in range(1,plateforms+1):
                prev_arrival_time = map[i]
                
                if prev_arrival_time < current_arrival_time:
                    map[i] = current_departure_time
                    break
            else:
                plateforms = plateforms + 1 
                map[plateforms] = current_departure_time
        
        return plateforms