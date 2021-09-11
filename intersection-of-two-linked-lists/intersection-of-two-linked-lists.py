"""
Time: O(N+M)
Space: O(N+M)
"""

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        setA={}
        setB={}
        
        currA=headA
        currB=headB
        
        while currA or currB:
            if currA==currB:
                return currA
            if currA:
                setA[currA]=True
                if currA in setB:
                    return currA
                currA=currA.next
            if currB:
                setB[currB]=True
                if currB in setA:
                    return currB
                currB=currB.next

        return
        
