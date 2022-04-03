# https://www.codingninjas.com/codestudio/guided-paths/data-structures-algorithms/content/118820/offering/1381870?leftPanelTab=0

from sys import stdin,setrecursionlimit
setrecursionlimit(10**7)

def maxSubarraySum(nums, n) :
    
    if not nums:
        return 0
    
    max_sum = 0 # Taking max sum = 0 instead of float(-"inf") because it is given  that 
                # we also have to take the sum of an empty set which = 0, so if all the 
                # elements are negative in the array our code should retrun 0 as the maxsum
                # of an empty sunarray.
        
    for i in range(len(nums)):
        for j in range(i,len(nums)):
                
            summ = 0
            for k in range(i,j+1):
                summ = summ + nums[k]
                    
            if summ > max_sum :
                max_sum = summ
    return max_sum

# taking inpit using fast I/O
def takeInput() :
	
    n =  int(input())

    if(n == 0) :
        return list(), n

    arr = list(map(int, stdin.readline().strip().split(" ")))

    return arr, n


# main
arr, n = takeInput()
print(maxSubarraySum(arr, n))
