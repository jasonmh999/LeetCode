"""
Time: O(N+M)
Space: O(N+M)
"""

class Solution:
    def minSteps(self, s: str, t: str) -> int:
        memo_s={}
        memo_t={}
        
        for char in s:
            memo_s[char]=memo_s.get(char,0)+1
        for char in t:
            memo_t[char]=memo_t.get(char,0)+1
    
        counter=0

        for key, value in memo_t.items():
            if key not in memo_s:
                counter+=value
            elif value>memo_s[key]:
                counter+=value-memo_s[key]
        return counter