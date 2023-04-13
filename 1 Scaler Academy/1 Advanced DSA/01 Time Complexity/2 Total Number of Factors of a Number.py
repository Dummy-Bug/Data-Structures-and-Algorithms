# https://practice.geeksforgeeks.org/problems/number-of-factors1435/1/#

class Solution:
    
    def countFactors (self, N):
        
        num = int(N**0.5)
        
        # print(N)
        count = 0
        for i in range(1,num+1):
            
            if (N)%i == 0: # if i is a factor
                
                
                if N//i == i: # if i is a prefect square
                    
                    count += 1
                else:
                    count += 2
        
        return count
            