
# https://www.codingninjas.com/codestudio/guided-paths/data-structures-algorithms/content/118820/offering/1381882?leftPanelTab=0

'''
   	Time Complexity - O(log N)
	Space Complexity - O(1)

	Where 'N' is the size of the array.
'''


def bestInsertPos(arr, n, m):

    lo = 0
    hi = n - 1
    ans = -1

    while lo <= hi:

        mid = lo + (hi - lo) // 2

        # Check if element is present.
        if (arr[mid] == m):
            return mid
        
        # Check the left half.
        if (arr[mid] > m):
            hi = mid - 1
            ans = mid
        # Check the right half.
        else:
            lo = mid + 1

    if (ans == -1):
        ans = n

    return ans