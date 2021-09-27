class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        ans=[]
        for i in range(1,numRows+1):
            if i==1:
                ans.append([1])
            else:
                previousRow=ans[i-2]
                temp=[]
                for j in range(0,len(previousRow)+1):
                    left = previousRow[j-1] if j-1 >= 0 else 0
                    right= previousRow[j] if j < len(previousRow) else 0
                    temp.append(left+right)
                
                ans.append(temp)
        
        return ans
            