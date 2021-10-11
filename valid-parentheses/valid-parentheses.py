"""
Time: O(N)
Space: O(N)
"""
class Solution:
    def isValid(self, s: str) -> bool:
        openType={'(','{','['}
        closeType={')':'(','}':'{',']':'['}
        stack=[]
        
        for paren in s:
            if paren in openType:
                stack.append(paren)
            elif paren in closeType:
                if not stack or stack.pop()!=closeType[paren]:
                    return False
        
        return not stack
