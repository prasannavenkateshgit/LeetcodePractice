'''
Given an integer array nums of unique elements, return all possible subsets (the power set).

The solution set must not contain duplicate subsets. Return the solution in any order.

 

Example 1:

Input: nums = [1,2,3]
Output: [[],[1],[2],[1,2],[3],[1,3],[2,3],[1,2,3]]
Example 2:

Input: nums = [0]
Output: [[],[0]]
'''
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        ans=[]
        def backtrack(curr,i):
            if i>len(nums):
                return
            ans.append(curr[:])
            for j in range(i,len(nums)):
                curr.append(nums[j])
                backtrack(curr,j+1)
                curr.pop()
        backtrack([],0)
        return ans
