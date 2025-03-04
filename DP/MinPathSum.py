'''
Given a m x n grid filled with non-negative numbers, find a path from top left to bottom right, which minimizes the sum of all numbers along its path.

Note: You can only move either down or right at any point in time.
'''
class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        def dp(r,c):
            if r+c==0:
                return grid[0][0]
            if (r,c) in memo:
                return memo[(r,c)]
            ans=float("inf")
            if r>0:
                ans=min(ans,dp(r-1,c)+grid[r][c])
            if c>0:
                ans=min(ans,dp(r,c-1)+grid[r][c])
            memo[(r,c)]=ans
            return memo[(r,c)]
        memo={}
        return dp(len(grid)-1,len(grid[0])-1)
