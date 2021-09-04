class Solution:
    def findFloor(self,a,N,x):
        low  =  0
        high =  N-1
        candidate = -1
        if a[low] > x:
            return -1
        elif a[high] <= x:
            return high
        while low <= high:

            mid = (low+high)//2
                
            if a[mid] == x:
                return mid
                
            elif a[mid] < x:
                candidate = mid
                low = mid + 1
                    
            elif a[mid] > x:
                high = mid - 1
        return candidate