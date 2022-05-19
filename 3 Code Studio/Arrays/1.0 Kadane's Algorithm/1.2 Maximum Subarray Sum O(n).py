# https://www.codingninjas.com/codestudio/guided-paths/data-structures-algorithms/content/118820/offering/1381870?leftPanelTab=0

from sys import stdin,setrecursionlimit
setrecursionlimit(10**7)

def maxSubarraySum(nums, n) :
    
        max_sum = 0
        current_sum = 0
        
        for element in nums:
            
            if element >= 0: # if element is positive then it will definitely increase the current sum
                current_sum = current_sum + element
                
            elif element < 0: # if element is negative then we can have two choices.
                  
                
                if current_sum + element >= 0: # if current_sum is still positive after adding the element then 
                                               # this current sum will surely increase the sum if added to the next elements
                    current_sum = current_sum + element
                
                else: # but if adding the element making the current_sum negative , then we should reset the sum because
                      # it will decrease our new summ.
                    current_sum = 0
            # consider a scenario where our current_sum = -5, and next element is +8, then it would have been better if we had
            # reset our current_sum becasue now this -5 when added to the next element making the whole sum = 3 only.
            max_sum = max(max_sum,current_sum)
            
        return max_sum


def takeInput() :
	
    n =  int(input())

    if(n == 0) :
        return list(), n

    arr = list(map(int, stdin.readline().strip().split(" ")))

    return arr, n


# main
arr, n = takeInput()
print(maxSubarraySum(arr, n))
