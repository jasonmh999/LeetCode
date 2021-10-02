# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        
        
        def dfs(node):
            if node is None:
                return 0

            left = dfs(node.left);

            if left==-1:
                return -1

            right = dfs(node.right);

            if right == -1 or abs(left - right) > 1:
                return -1

            return max(left, right) + 1
        
        return False if dfs(root)==-1 else True