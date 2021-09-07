"""
Time: O(N)
Space: O(1)
"""

class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        maxnumsset=set()
        
        for num in nums:
            maxnumsset.add(num)
            #remove smallest if more than 3
            if len(maxnumsset)>3:
                #finding min is O(1) because only set of 0-4
                maxnumsset.remove(min(maxnumsset))
        
        if len(maxnumsset)==3:
            return min(maxnumsset)
        return max(maxnumsset)