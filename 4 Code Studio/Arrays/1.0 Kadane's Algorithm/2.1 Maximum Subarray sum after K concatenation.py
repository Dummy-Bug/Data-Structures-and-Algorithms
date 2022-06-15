# O(n*k) + O(n*k) , first we are extending the array in O(n*k), then we are finding the max_sum in O(n)

# https://www.codingninjas.com/codestudio/guided-paths/data-structures-algorithms/content/118820/offering/1381873

def maxSubarraySum(nums, n) :
        max_sum = nums[0]
        current_sum = 0
        bool = False

        for element in nums:
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
    
    while k > 1:
        k = k - 1
        
        for i in range(n):
            arr.append(arr[i])
#     print(arr)    
    return maxSubarraySum(arr,len(arr))