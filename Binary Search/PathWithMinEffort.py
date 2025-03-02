'''
You are a hiker preparing for an upcoming hike. You are given heights, a 2D array of size rows x columns, where heights[row][col] represents the height of cell (row, col). You are situated in the top-left cell, (0, 0), and you hope to travel to the bottom-right cell, (rows-1, columns-1) (i.e., 0-indexed). You can move up, down, left, or right, and you wish to find a route that requires the minimum effort.

A route's effort is the maximum absolute difference in heights between two consecutive cells of the route.

Return the minimum effort required to travel from the top-left cell to the bottom-right cell.
'''
class Solution:
    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        def valid(row,col):
            return 0<=row<m and 0<=col<n
        
        def check(effort):
            directions=[(0,1),(1,0),(0,-1),(-1,0)]
            seen=set()
            seen.add((0,0))
            stack=[(0,0)]
            while stack:
                x,y=stack.pop()
                if (x,y)==(m-1,n-1):
                    return True
                for dx,dy in directions:
                    nr=x+dx
                    nc=y+dy
                    if valid(nr,nc) and (nr,nc) not in seen:
                        if abs(heights[nr][nc]-heights[x][y])<=effort:
                            seen.add((nr,nc))
                            stack.append((nr,nc))
            return False
        m=len(heights)
        n=len(heights[0])
        left=0
        right=max(max(row) for row in heights)
        while left<=right:
            mid=(left+right)//2
            if check(mid):
                right=mid-1
            else:
                left=mid+1
        return left
