'''
You are given a list of bombs. The range of a bomb is defined as the area where its effect can be felt. This area is in the shape of a circle with the center as the location of the bomb.

The bombs are represented by a 0-indexed 2D integer array bombs where bombs[i] = [xi, yi, ri]. xi and yi denote the X-coordinate and Y-coordinate of the location of the ith bomb, whereas ri denotes the radius of its range.

You may choose to detonate a single bomb. When a bomb is detonated, it will detonate all bombs that lie in its range. These bombs will further detonate the bombs that lie in their ranges.

Given the list of bombs, return the maximum number of bombs that can be detonated if you are allowed to detonate only one bomb.
'''
class Solution:
    def maximumDetonation(self, bombs: List[List[int]]) -> int:
        n=len(bombs)
        graph=defaultdict(list)
        for i in range(n):
            for j in range(n):
                if i==j:
                    continue
                xi,yi,ri=bombs[i]
                xj,yj,rj=bombs[j]
                if ri**2>=(xi-xj)**2+(yi-yj)**2:
                    graph[i].append(j)
        def dfs(node,visited):
            visited.add(node)
            for neigh in graph[node]:
                if neigh not in visited:
                    visited.add(neigh)
                    dfs(neigh,visited)
            return len(visited)
        
        ans=0
        for i in range(n):
            visited=set()
            ans=max(ans,dfs(i,visited))
        return ans
