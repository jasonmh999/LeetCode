class Solution:
    def numDifferentIntegers(self, word: str) -> int:
        ans=0
        tempInteger=''
        memo=set()
        
        i=0
        while i<len(word):
            while i<len(word) and not word[i].isdigit():
                i+=1
            while i<len(word) and word[i].isdigit():
                tempInteger+=word[i]
                i+=1
            if tempInteger!='' and int(tempInteger) not in memo:
                memo.add(int(tempInteger))
                ans+=1
            tempInteger=''
            
            
        return ans
            