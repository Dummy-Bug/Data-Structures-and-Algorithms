# https://www.codingninjas.com/codestudio/guided-paths/data-structures-algorithms/content/118820/offering/1381875?leftPanelTab=0

def sort012(arr, n) :# One simple solution could be just find the occurrence of each 
	                 # of the element and then place them accordingly O(n) but it requires two passes
	
	
	
	# First of all try to settle p0 and p2 such that arr[p0] != 0 and arr[p2] != 2,after that traverse the mid, if mid ==2 replace it
	# with p2 ,if mid = 0 replace it with p0.
	
	p0,mid,p2 = 0,0,n-1
	
	while mid <= p2:
		
		if mid < p0: 
			mid = p0
			continue 
		
		if arr[p0] == 0:
			p0 += 1
			continue 
		if arr[p2] == 2:
			p2 -= 1
			continue
		
		if arr[p2] == 0:
			arr[p0], arr[p2] = arr[p2], arr[p0]
			continue
		
		if arr[mid] == 0:
			arr[p0], arr[mid] = arr[mid], arr[p0]
			continue 
		
		if arr[mid] == 2:
			arr[mid], arr[p2] = arr[p2], arr[mid]
			continue
		
		mid = mid + 1