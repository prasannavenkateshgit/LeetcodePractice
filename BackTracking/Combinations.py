'''
Given two integers n and k, return all possible combinations of k numbers chosen from the range [1, n].

You may return the answer in any order.
'''
class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        def backtrack(curr,i):
            if len(curr)==k:
                ans.append(curr[:])
                return
            for j in range(i,n+1):
                if j not in curr:
                    curr.append(j)
                    backtrack(curr,j+1)
                    curr.pop()
        ans=[]
        backtrack([],1)
        return ans
