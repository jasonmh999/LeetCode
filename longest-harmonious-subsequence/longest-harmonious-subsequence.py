"""
Time: O(nlogn)
Space: O(logn)
"""

class Solution:
    def findLHS(self, nums: List[int]) -> int:
        if len(nums)==1:
            return 0
        nums.sort()
        answer=0
        
        right=1
        left=0
        
        while right<len(nums):
            while nums[right]-nums[left]>1:
                left+=1
            if nums[right]-nums[left]==1:
                answer=max(answer, right-left+1)
            right+=1
        return answer