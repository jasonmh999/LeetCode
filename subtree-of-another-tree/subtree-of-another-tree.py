"""
Time: O(N*M) [# of nodes of each tree]
Space: O(N+M)
"""
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        stringRoot = self.traverse(root)
        stringSubRoot = self.traverse(subRoot)
        if stringSubRoot in stringRoot:
            return True
        return False
    
    
    def traverse(self, node):
        if node:
            #add a special chacter so as to not 
            #accidently match substring
            # like '2' in '12'
            x=str(node.val)
            y=str(self.traverse(node.left))
            z=str(self.traverse(node.right))
            return '#'+x+y+z
        return None
