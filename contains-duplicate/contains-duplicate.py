class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        memo=set()
        for num in nums:
            if num in memo:
                return True
            else:
                memo.add(num)
        
        return False