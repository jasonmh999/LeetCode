"""
Time: O(N*M)
Space: O(1)
"""

class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        #set of rectangle perimeters that get smaller
        # startcol, endcol, startrow,endrow
        
        startrow=0
        endrow=len(matrix)-1
        startcol=0
        endcol=len(matrix[0])-1
        
        result=[]
        
        while startrow<=endrow and startcol<=endcol:
            for col in range(startcol, endcol+1):
                result.append(matrix[startrow][col])
            
            for row in range(startrow+1,endrow+1):
                result.append(matrix[row][endcol])
            
            #two edge cases; single row or single col left
            for col in reversed(range(startcol,endcol)):
                if startrow==endrow:
                    break
                result.append(matrix[endrow][col])
            
            for row in reversed(range(startrow+1,endrow)):
                if startcol==endcol:
                    break
                result.append(matrix[row][startcol])
            
            startrow+=1
            endrow-=1
            startcol+=1
            endcol-=1
        return result
                
            
            