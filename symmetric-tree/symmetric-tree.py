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
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        if root is None:
            return True
        
        stackleft=[root.left]
        stackright=[root.right]
        
        while stackleft or stackright:
            l=stackleft.pop()
            r=stackright.pop()
            
            if l is None and r is None:
                continue
            elif l is None or r is None:
                return False
            else:
                if l.val!=r.val:
                    return False
                stackleft.extend([l.left, l.right])
                stackright.extend([r.right,r.left])
        
        
        return True
        