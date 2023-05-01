# https://practice.geeksforgeeks.org/problems/median-in-a-row-wise-sorted-matrix1527/1/#

class Solution:

    def countSmallerThanMid(self, arr, mid):
        l = 0
        h = len(arr)-1

        while l <= h:
            md = (h+l) // 2

            if arr[md] <= mid:
                l = md + 1
            else:
                h = md - 1
        
        return l 

    def median(self, A, n, m):
        
        low = 1
        high = 2000

        while low <= high:
            mid = (high + low) // 2
            count = 0
            for i in range(n):
                count += self.countSmallerThanMid(A[i], mid)
            
            if count <= (n * m) // 2:
                low = mid + 1
            else:
                high = mid - 1
            
        
        return low