'''
Find all valid combinations of k numbers that sum up to n such that the following conditions are true:

Only numbers 1 through 9 are used.
Each number is used at most once.
Return a list of all possible valid combinations. The list must not contain the same combination twice, and the combinations may be returned in any order.
'''
class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        res=[]
        def backtrack(remain,comb,nextstart):
            if remain == 0 and len(comb)==k:
                res.append(list(comb))
                return
            elif remain<0 or len(comb)==k:
                return
            for i in range(nextstart,9):
                comb.append(i+1)
                backtrack(remain-i-1,comb,i+1)
                comb.pop()
        backtrack(n,[],0)
        return res
        
