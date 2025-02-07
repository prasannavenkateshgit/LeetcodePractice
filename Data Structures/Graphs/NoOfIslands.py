'''
Given an m x n 2D binary grid grid which represents a map of '1's (land) and '0's (water), return the number of islands.

An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically. You may assume all four edges of the grid are all surrounded by water.
'''
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        def valid_row(row,col):
            return 0<=row<m and 0<=col<n and grid[row][col]=="1"
        
        def dfs(row,col):
            for dx,dy in directions:
                next_row, next_col = row+dy, col+dx
                if valid_row(next_row, next_col) and (next_row, next_col) not in seen:
                    seen.add((next_row,next_col))
                    dfs(next_row, next_col)
        
        directions=[(0,1),(1,0),(0,-1),(-1,0)]
        m=len(grid)
        n=len(grid[0])
        seen=set()
        ans=0
        for i in range(m):
            for j in range(n):
                if grid[i][j]=="1" and (i,j) not in seen:
                    ans+=1
                    seen.add((i,j))
                    dfs(i,j)
        return ans
