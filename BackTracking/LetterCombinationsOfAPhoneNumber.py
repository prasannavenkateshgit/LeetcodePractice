'''
Given a string containing digits from 2-9 inclusive, return all possible letter combinations that the number could represent. Return the answer in any order.

A mapping of digits to letters (just like on the telephone buttons) is given below. Note that 1 does not map to any letters.
'''
class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if len(digits)==0:
            return []
        dic={"2":["a","b","c"],
            "3":["d","e","f"],
            "4":["g","h","i"],
            "5":["j","k","l"],
            "6":["m","n","o"],
            "7":["p","q","r","s"],
            "8":["t","u","v"],
            "9":["w","x","y","z"]}
        def backtrack(curr,i):
            if len(curr)==len(digits):
                ans.append(curr[:])
                return
            possible=dic[digits[i]]
            for c in possible:
                curr+=c
                backtrack(curr,i+1)
                curr=curr[:-1]
        ans=[]
        backtrack("",0)
        return ans
