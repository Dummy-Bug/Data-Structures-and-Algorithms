# O(n*k) but still giving TLE

#  https://www.codingninjas.com/codestudio/guided-paths/data-structures-algorithms/content/118820/offering/1381873?leftPanelTab=0


def maxSubarraySum(nums, n,k) :
        max_sum = nums[0]
        current_sum = 0
        bool = False

        for i in range(n*k):
            
            element = nums[i%n]
            
            if element >= 0: 
                current_sum = current_sum + element
                bool = True
                
            elif element < 0:
                if current_sum + element >= 0: 
                    current_sum = current_sum + element
                else: 
                    current_sum = 0
            if bool == True: # if True it means we atleast have encountered one positive number
                max_sum = max(max_sum,current_sum)
        
        if bool == False:
            return max(nums)
        return max_sum

def maxSubSumKConcat(arr, n, k):  
    return maxSubarraySum(arr,n,k)