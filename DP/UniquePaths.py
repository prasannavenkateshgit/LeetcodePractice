'''
There is a robot on an m x n grid. The robot is initially located at the top-left corner (i.e., grid[0][0]). The robot tries to move to the bottom-right corner (i.e., grid[m - 1][n - 1]). The robot can only move either down or right at any point in time.

Given the two integers m and n, return the number of possible unique paths that the robot can take to reach the bottom-right corner.

The test cases are generated so that the answer will be less than or equal to 2 * 109.
'''
class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        def dp(r,c):
            if r+c==0:
                return 1
            if (r,c) in memo:
                return memo[(r,c)]
            ways=0
            if r>0:
                ways+=dp(r-1,c)
            if c>0:
                ways+=dp(r,c-1)
            memo[(r,c)]=ways
            return memo[(r,c)]
        memo={}
        return dp(m-1,n-1)
