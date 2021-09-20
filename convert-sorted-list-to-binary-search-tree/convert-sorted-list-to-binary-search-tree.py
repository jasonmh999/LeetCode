"""
Time: O(N)
Space: O(N)
"""

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedListToBST(self, head: Optional[ListNode]) -> Optional[TreeNode]:
        if not head:
            return head
        
        
        node=head
        flattened=[]
        while node:
            flattened.append(node.val)
            node=node.next
        
        #find midpoint and recurse on both halfs
        
        def helper(left,right):
            if left>right:
                return None
            midpt=(left+right)//2
            node=TreeNode(flattened[midpt])
            
            #base case
            if left==right:
                return node
            node.left=helper(left,midpt-1)
            node.right=helper(midpt+1,right)
            return node
        newhead=helper(0,len(flattened)-1)
        return newhead