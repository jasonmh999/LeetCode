"""
Time O(not good)
Space O(1)
"""
class Solution:
    def sumOddLengthSubarrays(self, arr: List[int]) -> int:
        total=0
        
        for i in range(1,len(arr)+1,2): #size of window
            for j in range(len(arr)-i+1):
                total+=sum(arr[j:j+i])
        
        return total