class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        memo={}
        for index,num in enumerate(nums):
            if num in memo:
                compareIndex=memo.pop(num)
                if abs(compareIndex-index)<=k:
                    #check index compared to k
                    #if not found add index
                    return True
                else:
                    memo[num]=index
            else:
                memo[num]=index
                
                
                
        return False