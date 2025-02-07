'''
There are n cities. Some of them are connected, while some are not. If city a is connected directly with city b, and city b is connected directly with city c, then city a is connected indirectly with city c.

A province is a group of directly or indirectly connected cities and no other cities outside of the group.

You are given an n x n matrix isConnected where isConnected[i][j] = 1 if the ith city and the jth city are directly connected, and isConnected[i][j] = 0 otherwise.

Return the total number of provinces.
'''
class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        def dfs(node):
            for neighbor in graph[node]:
                if neighbor not in seen:
                    seen.add(neighbor)
                    dfs(neighbor)
        
        graph=defaultdict(list)
        for i in range(len(isConnected)):
            for j in range(i+1, len(isConnected[0])):
                if isConnected[i][j]:
                    graph[i].append(j)
                    graph[j].append(i)
        ans=0
        seen=set()
        for i in range(len(isConnected)):
            if i not in seen:
                ans+=1
                seen.add(i)
                dfs(i)
        return ans
