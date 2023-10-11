'''Letter combinations of a phone number-leetcode(17)'''
class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        d={'2':'abc','3':'def','4':'ghi','5':'jkl','6':'mno','7':'pqrs','8':'tuv','9':'wxyz'}
        res=[]
        def backtrack(i,combo):
            if len(combo)==len(digits):
                res.append(combo)
                return
            for letter in d[digits[i]]:
                backtrack(i+1,combo+letter)
        if digits:
            backtrack(0,'')
        return res
