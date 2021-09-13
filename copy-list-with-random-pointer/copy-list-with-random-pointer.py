"""
Time: O(N)
Space: O(N)
"""

"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Node') -> 'Node':
        memo={}
        
        if not head:
            return None

        newhead=Node(head.val)
        memo[head]=newhead
        last=newhead
        curr=head.next
        
        while curr:
            temp=Node(curr.val)
            memo[curr]=temp
            last.next=temp
            last=temp
            curr=curr.next

        #set random node
        curr=newhead
        reference=head
        while curr:
            if reference.random:
                curr.random=memo[reference.random]
            curr=curr.next
            reference=reference.next
                    
        return newhead
        
        