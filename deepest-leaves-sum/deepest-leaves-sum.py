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
    def deepestLeavesSum(self, root: Optional[TreeNode]) -> int:
        stack=[root]
        while stack:
            next_layer=[]
            temp=0
            for item in stack:
                temp+=item.val
                if item.left:
                    next_layer.append(item.left)
                if item.right:
                    next_layer.append(item.right)
            
            if next_layer==[]: #if no children
                return temp
            else:
                stack=next_layer
        
            
            