'''
You are given an m x n binary matrix grid. An island is a group of 1's (representing land) connected 4-directionally (horizontal or vertical.) You may assume all four edges of the grid are surrounded by water.

The area of an island is the number of cells with a value 1 in the island.

Return the maximum area of an island in grid. If there is no island, return 0.
'''
class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        def valid(row,col):
            return 0<=row<m and 0<=col<n and grid[row][col]==1
        
        def dfs(r,c):
            if not (0 <= r < len(grid) and 0 <= c < len(grid[0])
                    and (r, c) not in seen and grid[r][c]):
                return 0
            seen.add((r, c))
            return (1 + dfs(r+1, c) + dfs(r-1, c) +
                    dfs(r, c-1) + dfs(r, c+1))
        
        directions = [(1,0),(0,1),(-1,0),(0,-1)]
        seen=set()
        areas=[]
        m=len(grid)
        n=len(grid[0])
        for i in range(m):
            for j in range(n):
                areas.append(dfs(i,j))
        if areas:
            print(areas)
            return max(areas)
        else:
            return 0
