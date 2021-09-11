"""
Time: O(N)
Space: O(N)
"""

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: ListNode) -> ListNode:
        curr=head
        seen={}
        while curr:
            if curr in seen:
                return curr
            else:
                seen[curr]=True
                curr=curr.next
            
 
        return None