# https://practice.geeksforgeeks.org/problems/minimum-platforms-1587115620/1#
class Solution:    
    
    def minimumPlatform(self,n,arr,dep):
        aux_array = []
        
        for i in range(n):
            aux_array.append([arr[i],dep[i]])
        
        aux_array = sorted(aux_array,key = lambda x:x[0])
        # print(aux_array)
        from collections import deque
        plateforms = 1
        import heapq
        heap = []
        prev_departure_time = aux_array[0][1]
        heapq.heappush(heap,prev_departure_time) # store the latest departure time
        
        for i in range(1,n):
            
            current_arrival_time   = aux_array[i][0]
            current_departure_time = aux_array[i][1]
            
            prev_departure_time = heap[0]
            
            if prev_departure_time < current_arrival_time:
                heapq.heappop(heap)
                heapq.heappush(heap,current_departure_time)
            
            else:
                heapq.heappush(heap,current_departure_time)
                plateforms += 1
        
        return plateforms