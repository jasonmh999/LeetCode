"""
Time: O(N)
Space: O(N)
"""

"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def maxDepth(self, root: 'Node') -> int:
        depth=0
        if root is None:
            return 0
        
        previous_layer = [root]

        while previous_layer:
            depth+=1
            curr_layer = []
            for node in previous_layer:
                curr_layer.extend(node.children)
            previous_layer = curr_layer        
        
        return depth
            
            