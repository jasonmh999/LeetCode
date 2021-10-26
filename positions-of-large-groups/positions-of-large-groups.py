class Solution:
    def largeGroupPositions(self, s: str) -> List[List[int]]:
        output=[]
        grouprun=0
        run_begins=0
        prev_char=None
        for index,char in enumerate(s):
            if char==prev_char:
                if grouprun==0:
                    grouprun=1
                    run_begins=index-1
                grouprun+=1
            else:
                if grouprun>=3:
                    output.append([run_begins,index-1])
                grouprun=0
                prev_char=char
                    
        else:
            if grouprun>=3:
                output.append([run_begins,index])
        return output