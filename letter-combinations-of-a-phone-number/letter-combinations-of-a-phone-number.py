"""
Time: O(N*4^N)
Space: O(N)
"""

class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if digits=="":
            return []
        keys={'2':['a','b','c'],
             '3':['d','e','f'],
             '4':['g','h','i'], 
             '5':['j','k','l'], 
             '6':['m','n','o'], 
             '7':['p','q','r','s'], 
             '8':['t','u','v'], 
             '9':['w','x','y','z'], }
        
        def helper(idx,path):
            if len(path)==len(digits):
                combos.append("".join(path))
                return
            possibles=keys[digits[idx]]
            for letter in possibles:
                path.append(letter)
                helper(idx+1,path)
                path.pop()
            
        combos=[]
        helper(0,[])
        return combos