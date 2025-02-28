'''
You are given an m x n grid where each cell can have one of three values:

0 representing an empty cell,
1 representing a fresh orange, or
2 representing a rotten orange.
Every minute, any fresh orange that is 4-directionally adjacent to a rotten orange becomes rotten.

Return the minimum number of minutes that must elapse until no cell has a fresh orange. If this is impossible, return -1.
'''
class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        q=deque()
        time,fresh=0,0
        rows=len(grid)
        cols=len(grid[0])
        for i in range(rows):
            for j in range(cols):
                if grid[i][j]==1:
                    fresh+=1
                if grid[i][j]==2:
                    q.append((i,j))
        directions=[(0,1),(1,0),(0,-1),(-1,0)]
        while q and fresh>0:
            for i in range(len(q)):
                r,c=q.popleft()
                for dr,dc in directions:
                    row=dr+r
                    col=dc+c
                    if (row<0 or row==rows or col<0 or col==cols or grid[row][col]!=1):
                        continue
                    grid[row][col]=2
                    q.append((row,col))
                    fresh-=1
            time+=1
        return time if fresh==0 else -1
