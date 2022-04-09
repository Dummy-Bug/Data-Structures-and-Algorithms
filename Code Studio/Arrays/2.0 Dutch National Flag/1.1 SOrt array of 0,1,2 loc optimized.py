
# https://www.codingninjas.com/codestudio/guided-paths/data-structures-algorithms/content/118820/offering/1381875?leftPanelTab=0

def sort012(arr, n) :
	
	low,mid,high = 0, 0, n-1
	
	# use three pointers just like two pointers
	
	while mid <= high:
		
		if arr[mid] == 1:
			mid = mid + 1
			
		elif arr[mid] == 0:
			
			arr[mid], arr[low] = arr[low], arr[mid]
			low = low + 1
			mid = mid + 1
			
		elif arr[mid] == 2:
			arr[mid], arr[high] = arr[high],arr[mid]
			high = high - 1
		
# 		print(arr)