'''
You are given an m x n integer matrix grid where each cell is either 0 (empty) or 1 (obstacle). You can move up, down, left, or right from and to an empty cell in one step.

Return the minimum number of steps to walk from the upper left corner (0, 0) to the lower right corner (m - 1, n - 1) given that you can eliminate at most k obstacles. If it is not possible to find such walk return -1.
'''
class Solution:
    def shortestPath(self, grid: List[List[int]], k: int) -> int:
        def valid(r,c):
            return 0<=r<m and 0<=c<n
        
        directions=[(0,1),(1,0),(0,-1),(-1,0)]
        m=len(grid)
        n=len(grid[0])
        seen=set()
        que=collections.deque()
        que.append((0,0,k,0))
        while que:
            r,c,k,s=que.popleft()
            if r==m-1 and c==n-1:
                return s
            for x,y in directions:
                nr=r+y
                nc=c+x
                if valid(nr,nc):
                    if grid[nr][nc]==0:
                        if (nr,nc,k) not in seen:
                            seen.add((nr,nc,k))
                            que.append([nr,nc,k,s+1])
                    elif k and (nr,nc,k-1) not in seen:
                        seen.add((nr,nc,k-1))
                        que.append([nr,nc,k-1,s+1])
        return -1
