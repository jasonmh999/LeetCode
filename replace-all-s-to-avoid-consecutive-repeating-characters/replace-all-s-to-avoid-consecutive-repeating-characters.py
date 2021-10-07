class Solution:
    def modifyString(self, s: str) -> str:
        prev=''
        s=list(s)
        
        for index,char in enumerate(s):
            newchar=char
            if char=="?":
                newchar='a'
                nextChar=s[index+1] if index<len(s)-1 else ''
                if prev=='a' or nextChar=='a':
                    if prev=='b' or nextChar=='b':
                        newchar='c'
                    else:
                        newchar='b'
                s[index]=newchar
                
            prev=newchar
        
        return ''.join(s)