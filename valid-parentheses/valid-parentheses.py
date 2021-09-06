"""
Time: O(N)
Space: O(N)
"""
class Solution:
    def isValid(self, s: str) -> bool:
        openType={'(':0,'{':0,'[':0}
        closeType={')':'(','}':'{',']':'['}
        
        stack=[]
        for char in s:
            if char in openType:
                openType[char]+=1
                stack.append(char)
            elif char in closeType:
                if openType[closeType[char]]==0:
                    return False
                else:
                    openType[closeType[char]]-=1

                #check closing order
                lastbracket=stack.pop()
                if lastbracket!=closeType[char]:
                    return False
                
        for key,value in openType.items():
            if value>0:
                return False
        
        return True