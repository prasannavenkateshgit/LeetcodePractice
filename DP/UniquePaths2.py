'''
You are given an m x n integer array grid. There is a robot initially located at the top-left corner (i.e., grid[0][0]). The robot tries to move to the bottom-right corner (i.e., grid[m - 1][n - 1]). The robot can only move either down or right at any point in time.

An obstacle and space are marked as 1 or 0 respectively in grid. A path that the robot takes cannot include any square that is an obstacle.

Return the number of possible unique paths that the robot can take to reach the bottom-right corner.

The testcases are generated so that the answer will be less than or equal to 2 * 109.
'''
class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        def dp(row,col):
            if row+col==0:
                return 1
            if (row,col) in memo:
                return memo[(row,col)]
            ways=0
            if row>0:
                if obstacleGrid[row-1][col]!=1:
                    ways+=dp(row-1,col)
            if col>0:
                if obstacleGrid[row][col-1]!=1:
                    ways+=dp(row,col-1)
            memo[(row,col)]=ways
            return memo[(row,col)]
        memo={}
        m=len(obstacleGrid)-1
        n=len(obstacleGrid[0])-1
        if obstacleGrid[m][n]==1:
            return 0
        return dp(len(obstacleGrid)-1,len(obstacleGrid[0])-1)
