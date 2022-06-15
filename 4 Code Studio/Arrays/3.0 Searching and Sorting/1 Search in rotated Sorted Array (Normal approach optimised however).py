# https://www.codingninjas.com/codestudio/guided-paths/data-structures-algorithms/content/118820/offering/1381878?leftPanelTab=0


def search(nums, target) :
	
# Try to find out the mid first and then find the position of the element 

    ln = len(nums)
        
    pivot = getPivot(nums)
        
    low = pivot
    hi  = pivot + ln - 1
	
    while low <= hi:
		
        mid = (low + hi)//2 
        middle = mid%ln 
        if nums[middle] == target:
            return middle
		
        elif nums[middle] > target:
            hi = mid - 1
        else:
            low = mid + 1          
    return -1
def getPivot(nums):
	
    low = 0
    hi  = len(nums)-1
	
	# Try to solve binary search when low <= hi , you will get more clarity.
	# we can also think of this function as finding where the smallest value lies in the array, as it will 
    # tell us the begining of the array and then we can use modulus operator to get the position of the element.
    while low <= hi: # we have to use make it <= because when the array size if 1 then it will return low
		
        mid = (low+hi)//2
            
        if nums[mid] >= nums[low] and nums[mid] <= nums[hi]: 
            return low # return low as we want the index of smallest value in the array.
        else: 
            if  nums[mid] > nums[hi]: 
                low = mid + 1
                
            elif nums[mid] < nums[hi]:
                hi = mid
			
			
	