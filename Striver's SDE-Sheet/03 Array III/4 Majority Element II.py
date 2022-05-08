# https://leetcode.com/problems/majority-element-ii/

class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        element1, element2, cnt1, cnt2 = 0, 0, 0, 0
        for e in nums:
            if element1 == e:
                cnt1 += 1
            elif element2 == e:
                cnt2 += 1
            elif cnt1 == 0:
                element1, cnt1 = e, 1
            elif cnt2 == 0:
                element2, cnt2 = e, 1
            else:
                cnt1 -= 1
                cnt2 -= 1

        cnt1 = cnt2 = 0
        for e in nums:
            if element1 == e:
                cnt1 += 1
            elif element2 == e:
                cnt2 += 1

        ans = []
        if cnt1 > len(nums) // 3:
            ans += [element1]
        if cnt2 > len(nums) // 3:
            ans += [element2]

        return ans