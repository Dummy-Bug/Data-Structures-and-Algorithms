# https://leetcode.com/problems/median-of-two-sorted-arrays/
class Solution:
    def findMedianSortedArrays(self,arr1, arr2):
        n1 = len(arr1)
        n2 = len(arr2)

        if n1 > n2:
            arr1, arr2 = arr2, arr1
            n1, n2 = n2, n1

        low = 0
        high = n1

        while low <= high:
            cut1 = low + (high - low) // 2 
            cut2 = (n1 + n2 + 1) // 2 - cut1 

            l1 = -float('inf') if cut1 == 0 else arr1[cut1-1]
            l2 = -float('inf') if cut2 == 0 else arr2[cut2-1]

            r1 = float('inf') if cut1 == n1 else arr1[cut1]
            r2 = float('inf') if cut2 == n2 else arr2[cut2]

            if l1 <= r2 and l2 <= r1:
                if (n1+n2)%2 == 0:
                    return (max(l1, l2) + min(r1, r2)) / 2
                else:
                    return max(l1, l2)
            elif l1 > l2:
                high = cut1 - 1
            else:
                low = cut1 + 1

        return -1