"""
Time: O(N)
Space: O(1) #because only lowercase English letters stored in hashes
"""
from collections import OrderedDict

class Solution:
    def firstUniqChar(self, s: str) -> int:
        seenOnce=OrderedDict()
        seen={}
        
        for index,char in enumerate(s):
            if char not in seen:
                seen[char]=True
                seenOnce[char]=index
            elif char in seenOnce:
                seenOnce.pop(char)
                
        if seenOnce:
            return seenOnce.popitem(last=False)[1]
        else:
            return -1