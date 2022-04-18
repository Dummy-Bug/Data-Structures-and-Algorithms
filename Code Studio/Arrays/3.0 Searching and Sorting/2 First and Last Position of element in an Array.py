# https://www.codingninjas.com/codestudio/guided-paths/data-structures-algorithms/content/118820/offering/1381880?leftPanelTab=0

"""
Naively find first and the last occurrence
Create two storage variables IDX1 and idx2 to store the first and last position of occurrence and initialise them to -1.
Iterate through the array, if you encounter an array element equal to value X, and IDX1 = IDX2 = -1 previously, then update IDX1, IDX2 to the current index.
If IDX1 != -1 and you encounter an array element equal to value X, then only update IDX2 as then you had already recorded the first occurrence
Finally, return IDX1 and IDX2.
Time Complexity
O(N), where N is the size of the sorted array.

 

Since here a linear search is being used for traversing and searching through all the N elements of the sorted array, therefore, the worst-case time complexity becomes O(N). 

Space Complexity
O(1), as we are using constant extra memory.

"""
# Binary Search
# The given input array is sorted, thus we can apply binary search to the array. Binary search finds any element in O(log(N)), where N is the size of the input array.
# Binary search prunes the search space by a factor of 2, in every step. Thus, we choose a mid-index to compare the elements in the current range [LO, HI]. The maximum depth of the binary search call stack is O(log(N)).
'''
	Time Complexity: O(log(N))
	Space Complexity: O(1)

	Where N is the size of the sorted array.
'''

from sys import stdin, stdout, setrecursionlimit

setrecursionlimit(10 ** 7)

def findFirstLastPosition(arr, n, x):
    
	first = get_first_occurrence(arr,0,n-1,x)
	last  = get_last_occurrence(arr,0,n-1,x)
	
	return [first,last]

def get_first_occurrence(arr,low,high,x):
	
	first_index = -1 
	
	while low <= high :
		
		mid = (low+high)//2
		
		if arr[mid] == x:
			first_index = mid
			high = mid - 1   # keep moving left to check if it appears on the left side or not.
			
		elif arr[mid] < x:
			low = mid + 1
		else:
			high = mid - 1
	
	return first_index 


def get_last_occurrence(arr,low,high,x):
	
	last_index = -1 
	
	while low <= high :
		
		mid = (low+high)//2
		
		if arr[mid] == x:
			last_index = mid
			low = mid + 1   # keep moving right to check if it appears on the right side or not.
			
		elif arr[mid] < x:
			low = mid + 1
		else:
			high = mid - 1
	
	return last_index 

# Taking input using fast I/0.
def takeInput():
    N = int(stdin.readline())
    arr = list(map(int, stdin.readline().strip().split(" ")))
    X = int(stdin.readline())
    return N, arr, X

tc = int(input())
while tc > 0:
    N, arr, X = takeInput()
    ans = findFirstLastPosition(arr, N, X)
    stdout.write(str(ans[0]) + " " + str(ans[1]) + "\n")
    tc -= 1
