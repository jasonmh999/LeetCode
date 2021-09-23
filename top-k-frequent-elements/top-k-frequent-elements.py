"""
Time: O(n + k*log(n))
Space: O(N+k)
"""

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        #return most frequent popping off k times
        #heap sorted by frequency?
        
        memo={}
        for num in nums:
            memo[num]=memo.get(num,0)+1
        heap = []
        
        for key,value in memo.items():
            heap.append((value*-1, key))

        heapq.heapify(heap)
        print(heap)
        ans=[]
        for i in range(k):
            ans.append(heapq.heappop(heap)[1])

        return ans
