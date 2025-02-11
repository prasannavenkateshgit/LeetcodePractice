'''
Given an m x n binary matrix mat, return the distance of the nearest 0 for each cell.

The distance between two cells sharing a common edge is 1.
'''
import collections
class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        def valid(r,c):
            return 0<=r<m and 0<=c<n and mat[r][c]==1

        directions=[(0,1),(1,0),(0,-1),(-1,0)]
        seen=set()
        que=collections.deque()
        m=len(mat)
        n=len(mat[0])

        for i in range(m):
            for j in range(n):
                if mat[i][j]==0:
                    que.append((i,j,1))
                    seen.add((i,j))
        while que:
            r,c,s=que.popleft()
            for x,y in directions:
                nr,nc=r+y,c+x
                if (nr,nc) not in seen and valid(nr,nc):
                    seen.add((nr,nc))
                    que.append((nr,nc,s+1))
                    mat[nr][nc]=s
        return mat
