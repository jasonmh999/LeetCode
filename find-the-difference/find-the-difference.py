"""
Time: O(N)
Space: O(1)
"""

class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        memo_s={}
        for char in s:
            memo_s[char]=memo_s.get(char, 0) + 1

        for char in t:
            if char not in memo_s or memo_s[char]==0:
                return char
            else:
                memo_s[char]-=1