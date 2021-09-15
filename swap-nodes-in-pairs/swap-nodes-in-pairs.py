"""
Time: O(N)
Space: O(1)
"""

# Definition for singly-linked list.
# class ListNode:1
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        first=head
        second=head.next if head else None
        head=second if second else first
        previous=None
        
        while first and second:            
            first.next=second.next
            second.next=first

            if not previous:
                previous=first
            else:
                previous.next=second
                previous=first
                
            first=first.next
            second=first.next if first else None


            
        return head