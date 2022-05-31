# https://practice.geeksforgeeks.org/problems/job-sequencing-problem-1587115620/1#
'''
Time Complexity: O(N log N) + O(N*M).

O(N log N ) for sorting the jobs in decreasing order of profit. 
O(N*M) since we are iterating through all N jobs and for every job we are 
checking from the last deadline, say M deadlines in the worst case.

Space Complexity: O(M) for an array that keeps track on which day which job
is performed if M is the maximum deadline available.
'''
# T(c) will never be O(N*N) because M will never be equal to N
# Just look at the constraints deadline are always <= 100 
# Hence O(M*N) will never touch O(N*N)
# Thus Final complexity will always be O(NlogN)
class Solution:
    
    def JobScheduling(self,jobs,n):
        # here jobs is list that contains job objects
        jobs.sort(key = lambda x:x.profit,reverse = True)
        job_count = 0; total_profit = 0
        
        slot = [0]*101
        
        for job_obj in jobs:
            job_id,deadline,profit = job_obj.id,job_obj.deadline,job_obj.profit
            
            # print(profit,deadline,job_id)
            
            for i in range(deadline,0,-1):
                
                if slot[i] == 0: # means slot is empty
                    
                    slot[i] = job_id
                    job_count += 1
                    total_profit += profit
                    break
                # else keep on decreasing the deadline 
                # till we find an empty slot 
        # print(slot)
        return [job_count,total_profit]