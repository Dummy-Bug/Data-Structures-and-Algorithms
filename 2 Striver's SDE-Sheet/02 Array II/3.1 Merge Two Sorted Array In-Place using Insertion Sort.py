# https://practice.geeksforgeeks.org/problems/merge-two-sorted-arrays-1587115620/1#
# https://www.youtube.com/watch?v=hVl2b3bLzBw&list=PLgUwDviBIf0rPG3Ictpu74YWBQ1CaBkm2&index=5

class Solution:
    def merge(self,arr1,arr2,n,m):
        
        for i in range(n):
            j = 0
            
            if arr1[i] > arr2[j]:
                
                arr1[i], arr2[j] = arr2[j], arr1[i]

                while j < m-1 : # loop till the right position is not found.
                    
                    if arr2[j] > arr2[j+1]:
                        
                        x = arr2[j]
                        arr2[j] = arr2[j+1]
                        arr2[j+1] = x
                    else:
                        break
                    j = j + 1