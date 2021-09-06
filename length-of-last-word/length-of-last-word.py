"""
Time: O(N)
Space: O(1)
"""
class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        word=0
        for i in range(len(s)-1, -1, -1):
            if s[i]!=' ':
                word+=1
            elif word>0:
                break            
        
        return word