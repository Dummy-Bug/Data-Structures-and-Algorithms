class Solution:
    def JobScheduling(self,jobs,n):
        
        jobs.sort(reverse = True, key = lambda x:x.profit)
        
        max_deadline = 0
        
        for i in range(len(jobs)):
            max_deadline = max(max_deadline,jobs[i].deadline)
        
        job_count = 0
        slots     = [0]*max_deadline
        
        for object in jobs:
            
            dead   = object.deadline
            profit = object.profit
            
            for j in range(min(dead-1,max_deadline-1),-1,-1):
                
                if  slots[j] == 0 :
                    slots[j]  = profit
                    job_count = job_count + 1
                    break
                
        return (job_count,sum(slots))
