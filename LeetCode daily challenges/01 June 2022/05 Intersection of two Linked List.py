# https://leetcode.com/problems/intersection-of-two-linked-lists/
class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        
        lenA, lenB = 0, 0
        ptrA = headA ; ptrB = headB
        
        while ptrA:
            lenA += 1
            ptrA = ptrA.next
            
        while ptrB:
            lenB += 1
            ptrB = ptrB.next

        while lenA > lenB:
            headA = headA.next
            lenA -= 1
        
        while lenB > lenA:
            headB = headB.next
            lenB -= 1
        
        while headA != headB :
            headA = headA.next
            headB = headB.next
        return headA