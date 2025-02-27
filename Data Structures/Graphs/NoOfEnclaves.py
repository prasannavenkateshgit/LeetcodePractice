'''
You are given an m x n binary matrix grid, where 0 represents a sea cell and 1 represents a land cell.

A move consists of walking from one land cell to another adjacent (4-directionally) land cell or walking off the boundary of the grid.

Return the number of land cells in grid for which we cannot walk off the boundary of the grid in any number of moves.
'''
class Solution:
    def numEnclaves(self, grid: List[List[int]]) -> int:
        def dfs(r,c):
            if (r<0 or c<0 or r==m or c==n or not grid[r][c] or (r,c) in seen):
                return 0
            seen.add((r,c))
            res=1
            directions=[(0,1),(1,0),(0,-1),(-1,0)]
            for dr,dc in directions:
                res+=dfs(r+dr,c+dc)
            return res
        m=len(grid)
        n=len(grid[0])
        seen=set()
        land,border=0,0
        for i in range(m):
            for j in range(n):
                land+=grid[i][j]
                if (grid[i][j] and (i,j) not in seen and (j in [0,n-1] or i in [0,m-1])):
                    border+=dfs(i,j)

        return land-border
