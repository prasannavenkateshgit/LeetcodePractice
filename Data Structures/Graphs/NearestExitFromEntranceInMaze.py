'''
You are given an m x n matrix maze (0-indexed) with empty cells (represented as '.') and walls (represented as '+'). You are also given the entrance of the maze, where entrance = [entrancerow, entrancecol] denotes the row and column of the cell you are initially standing at.

In one step, you can move one cell up, down, left, or right. You cannot step into a cell with a wall, and you cannot step outside the maze. Your goal is to find the nearest exit from the entrance. An exit is defined as an empty cell that is at the border of the maze. The entrance does not count as an exit.

Return the number of steps in the shortest path from the entrance to the nearest exit, or -1 if no such path exists.
'''
class Solution:
    def nearestExit(self, maze: List[List[str]], entrance: List[int]) -> int:
        def valid(r,c):
            return 0<=r<m and 0<=c<n and maze[r][c]!="+"
        
        m=len(maze)
        n=len(maze[0])
        directions=[(1,0),(0,1),(-1,0),(0,-1)]
        seen=set()
        que=collections.deque()
        que.append((entrance[0],entrance[1],0))
        seen.add((entrance[0],entrance[1]))
        while que:
            r,c,step=que.popleft()
            if r==0 or c==0 or r==m-1 or c==n-1:
                if (r,c)!=(entrance[0],entrance[1]):
                    return step
            for x,y in directions:
                nr=r+y
                nc=c+x
                if valid(nr,nc) and (nr,nc) not in seen:
                    seen.add((nr,nc))
                    que.append((nr,nc,step+1))
        return -1
