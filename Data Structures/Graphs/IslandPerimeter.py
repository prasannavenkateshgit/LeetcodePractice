'''
You are given row x col grid representing a map where grid[i][j] = 1 represents land and grid[i][j] = 0 represents water.

Grid cells are connected horizontally/vertically (not diagonally). The grid is completely surrounded by water, and there is exactly one island (i.e., one or more connected land cells).

The island doesn't have "lakes", meaning the water inside isn't connected to the water around the island. One cell is a square with side length 1. The grid is rectangular, width and height don't exceed 100. Determine the perimeter of the island.
'''
class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        def valid(row,col):
            return 0<=row<m and 0<=col<n and grid[row][col]==1
        m=len(grid)
        n=len(grid[0])
        perimeter=0
        for i in range(m):
            for j in range(n):
                if grid[i][j]==1:
                    contri=4
                    if valid(i+1,j):
                        contri-=1
                    if valid(i,j+1):
                        contri-=1
                    if valid(i-1,j):
                        contri-=1
                    if valid(i,j-1):
                        contri-=1
                    perimeter+=contri
        return perimeter
