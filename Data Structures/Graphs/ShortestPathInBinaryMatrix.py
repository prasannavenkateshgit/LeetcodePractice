'''
Given an n x n binary matrix grid, return the length of the shortest clear path in the matrix. If there is no clear path, return -1.

A clear path in a binary matrix is a path from the top-left cell (i.e., (0, 0)) to the bottom-right cell (i.e., (n - 1, n - 1)) such that:

All the visited cells of the path are 0.
All the adjacent cells of the path are 8-directionally connected (i.e., they are different and they share an edge or a corner).
The length of a clear path is the number of visited cells of this path.
'''
class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        if grid[0][0]==1:
            return -1
        def valid(r,c):
            return 0<=r<n and 0<=c<n and grid[r][c]==0
        n=len(grid)
        seen=set()
        seen.add((0,0))
        que=collections.deque([(0,0,1)])
        directions=[(0,1),(1,0),(0,-1),(-1,0),(1,1),(1,-1),(-1,1),(-1,-1)]
        while que:
            curr=len(que)
            for i in range(curr):
                row,col,step=que.popleft()
                if row==n-1 and col==n-1:
                    return step
                for j,k in directions:
                    nr=row+k
                    nc=col+j
                    if valid(nr,nc) and (nr,nc) not in seen:
                        seen.add((nr,nc))
                        que.append((nr,nc,step+1))
        return -1
