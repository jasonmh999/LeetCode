from collections import namedtuple

class Solution:
    def canCross(self, stones: List[int]) -> bool:
        #nextJump k-1, k, k+1
        lastStone=stones[-1]
        currStone=stones[1]
        if currStone!=1:
            return False #no path
        Position = namedtuple("Position", "index jump")
        possibleJumps=[Position(1,1)]
        attemptedJumps=set()
        attemptedJumps.update(possibleJumps)
        stones=set(stones)
        while possibleJumps:
            currStone,jump=possibleJumps.pop()
            #print(currStone,jump)
            if currStone==lastStone:
                return True
            else:
                newJumps=[Position(currStone+jump+_, jump+_) for _ in range(-1,2) if jump+_>0 and jump+_<=lastStone and currStone+jump+_ in stones and Position(currStone+jump+_, jump+_) not in attemptedJumps]
                possibleJumps+=newJumps
                attemptedJumps.update(newJumps)

        return False
        
        
        
        