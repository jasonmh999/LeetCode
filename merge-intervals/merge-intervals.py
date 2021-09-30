class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()
        
        iterator=iter(intervals)
        ans=[next(iterator)]
        for interval in iterator:
            if ans[-1][1]<interval[0]:
                ans.append(interval)
            else:
                ans[-1][1]=max(ans[-1][1],interval[1])
                
        return ans