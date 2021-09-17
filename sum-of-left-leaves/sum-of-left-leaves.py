"""
Time: O(N)
Space: O(N)
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0
        stack=[root]
        
        total=0
        
        while stack:
            curr=stack.pop()
            if curr:
                if curr.left and curr.left.left is None and curr.left.right is None:
                    total+=curr.left.val
                stack.extend([curr.left,curr.right])
        
        return total
                