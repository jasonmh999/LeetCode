"""
could bucket search for all possible times bool[24*60]
search in both directions [count from begin and to end and check those two specially]
#if already seen that's the answer [0]
#else if see distance 1 that's the answer
"""
class Solution:
    def findMinDifference(self, timePoints: List[str]) -> int:
        bucket=[False for _ in range(24*60)]
        #want the bucket to sort for free basically
        
        for timePt in timePoints:
            time=int(timePt[:2])*60+int(timePt[3:5])
            if bucket[time]:
                return 0
            else:
                bucket[time]=True
        
        
        minTime=9000
        firstTime=True
        prevTime=0
        time_from_beginning=0
        for time, _ in filter(lambda x:x[1], enumerate(bucket)):
            if firstTime:
                prevTime=time
                time_from_beginning=time
                firstTime=False
            else:
                minTime=min(minTime, time-prevTime)
                #or clockwise??
                if minTime==1:
                    return 1
                prevTime=time
        else: #check last time
            minTime=min(minTime, time_from_beginning+1440-time)
            
        return minTime
                
            