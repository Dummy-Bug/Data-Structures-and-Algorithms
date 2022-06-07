# https://practice.geeksforgeeks.org/problems/allocate-minimum-number-of-pages0937/1
class Solution:
    
    def check_pages(self,arr,n,m,mid):
        students = 1
        sum = 0
        for i in range(n):
            sum = sum + arr[i]
            if sum> mid:
                sum = arr[i]
                students = students + 1
                
                if students > m:
                    return False
        return True
    
    
    def findPages(self,arr, n, m):
        low  = max(arr)
        high = sum(arr)
        result = -1
        if m>n:
            return result
        while low<= high:
            mid = (low+high)>>1
            
            if self.check_pages(arr,n,m,mid):
                result = mid
                high = mid - 1
            else:
                low  = mid + 1
        return result