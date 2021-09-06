"""
Time: O(N)
Space: 0(1)
"""

class Solution:
    def maxRepeating(self, sequence: str, word: str) -> int:
        if len(word)>len(sequence):
            return 0
        
        maxk=0
        i=0
        while i<len(sequence)-len(word)+1:
            j=i
            k=0 #times repeating
            while j<len(sequence)-len(word)+1 and sequence[j:j+len(word)]==word:
                j+=len(word)
                k+=1
            maxk=max(maxk,k)
            i+=1
        
        return maxk