"""
Time: O(max(N,M))
Space: O(max(N,M))
"""

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        carry=False
        returnlist=ListNode(0)
        currlist=returnlist
        while(True):
            digit=0
            if carry:
                digit=1
                carry=False
            if l1 is not None:
                digit+=l1.val
                l1=l1.next
            if l2 is not None:
                digit+=l2.val
                l2=l2.next
            #add digit to new list            
            #1. check if larger than 10
            if digit>9:
                carry=True
                digit-=10
            #2 add new digit
            currlist.val=digit


            if  l1 is None and l2 is None:
                if carry:
                    currlist.next=ListNode(None)
                    currlist=currlist.next
                    currlist.val=1
                break
            else:
                currlist.next=ListNode(None)
                currlist=currlist.next


            
            
        return returnlist