'''
Given an array of distinct integers candidates and a target integer target, return a list of all unique combinations of candidates where the chosen numbers sum to target. You may return the combinations in any order.

The same number may be chosen from candidates an unlimited number of times. Two combinations are unique if the frequency of at least one of the chosen numbers is different.

The test cases are generated such that the number of unique combinations that sum up to target is less than 150 combinations for the given input.
'''
class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        def backtrack(path,start,curr):
            if curr==target:
                ans.append(path[:])
                return
            for i in range(start,len(candidates)):
                num=candidates[i]
                if curr+num<=target:
                    path.append(num)
                    backtrack(path,i,curr+num)
                    path.pop()
        ans=[]
        backtrack([],0,0)
        return ans
