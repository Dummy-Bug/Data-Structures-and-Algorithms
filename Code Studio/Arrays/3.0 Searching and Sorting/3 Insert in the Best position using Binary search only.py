# https://www.codingninjas.com/codestudio/guided-paths/data-structures-algorithms/content/118820/offering/1381882?leftPanelTab=0

"""
Brute Force

Iterate through the given array.
If at any position i, we get A[i] ≥ M, return i.
If there is no such position i, return N.
Time Complexity
O(N), where ‘N’ is the length of the given array.

 

We are traversing the array only once. Hence, the overall complexity is O(N).

Space Complexity
O(1).

 

As there is no extra space required."""


def bestInsertPos(arr, n, m):
    
	if not arr:
		return 0
	
	if m < arr[0]:
		return 0
	elif m > arr[-1]:
		return n
		
	result = insert_pos(arr,0,n-1,m)
	return result
	

def insert_pos(arr,low,high,x):
	
	while low <= high:
		
		mid = (low+high)//2

		if arr[mid] == x:
			return mid
		elif (high-low+1) <= 2:
			result =  get_result(arr,low,high,x)
			return result

		elif arr[mid] < x and arr[mid+1] > x:
			return (mid+1)
		elif arr[mid] > x and arr[mid-1]< x:
			return (mid)
		elif arr[mid] > x:
			high = mid - 1
		elif arr[mid] < x:
			low = mid + 1
			
def get_result(arr,low,high,x):

	if arr[low] < x and x < arr[high]:
		return high
	elif arr[low] > x:
		return low 
	elif arr[high] < x:
		return (high+1)
	else:
		return (low+1)
	
		