"""
how to handle 11 and 12?

"""

class Solution:
    def numberToWords(self, num: int) -> str:
        ans=[]
        singleDigit={
            0:"Zero",
            1:"One",
            2:"Two",
            3:"Three",
            4:"Four",
            5:"Five",
            6:"Six",
            7:"Seven",
            8:"Eight",
            9:"Nine"
        }
        tenth={
            1:"Yelp",
            2:"Twenty",
            3:"Thirty",
            4:"Forty",
            5:"Fifty",
            6:"Sixty",
            7:"Seventy",
            8:"Eighty",
            9:"Ninety"
        }
        special={
            10:"Ten",
            11:"Eleven",
            12:"Twelve",
            13:"Thirteen",
            14:"Fourteen",
            15:"Fifteen",
            16:"Sixteen",
            17:"Seventeen",
            18:"Eighteen",
            19:"Nineteen"
        }
        
        def threeDigits(number):
            temp=[]
            if number>99:
                temp.append(singleDigit[number//100] + " Hundred")
                number=number%100
            if number//10>0:
                if number<20:
                    temp.append(special[number])
                    number=0
                else:
                    temp.append(tenth[number//10])
                    number=number%10
            if number>0:
                temp.append(singleDigit[number])
            return ' '.join(temp)
            
        if num==0:
            return "Zero"
        if num>=10**9:
            ans.append(threeDigits(num//10**9)+" Billion")
            num=num%10**9
        if num>=10**6:
            ans.append(threeDigits(num//10**6)+" Million")
            num=num%10**6
        if num>=10**3:
            ans.append(threeDigits(num//10**3)+" Thousand")
            num=num%10**3
        if num>0:
            ans.append(threeDigits(num))
        
            
        print(ans)    
        return " ".join(ans) if len(ans)>1 else str(ans[0])
            