"""
Time: O(N)
Space: O(N) #or k for num of digits?
"""

class Solution:
    def myAtoi(self, s: str) -> int:
        x=0
        negative=False
        
        i=0
        #ignore leading whitespace
        while i<len(s) and s[i]==' ':
            i+=1
        if i>=len(s):
            return 0

        if s[i]=='-':
            negative=True
            i+=1
        elif s[i]=='+':
            i+=1
        
        if i>=len(s):
            return 0
        
        number=[]
        while i<len(s) and s[i].isdigit():
            number.append(int(s[i]))
            i+=1

        if not number:
            return 0
        
        power=0
        for i in range(len(number)-1, -1, -1):
            x+=number[i]*10**power
            power+=1

        #check 32 bit range
        if negative:
            x*=-1
            if x<-2**31:
                x=-1*2**31
        else:
            if x>2**31-1:
                x=2**31-1

        
        
        return x