'''
You are given an integer n, the number of nodes in a directed graph where the nodes are labeled from 0 to n - 1. Each edge is red or blue in this graph, and there could be self-edges and parallel edges.

You are given two arrays redEdges and blueEdges where:

redEdges[i] = [ai, bi] indicates that there is a directed red edge from node ai to node bi in the graph, and
blueEdges[j] = [uj, vj] indicates that there is a directed blue edge from node uj to node vj in the graph.
Return an array answer of length n, where each answer[x] is the length of the shortest path from node 0 to node x such that the edge colors alternate along the path, or -1 if such a path does not exist.
'''
class Solution:
    def shortestAlternatingPaths(self, n: int, redEdges: List[List[int]], blueEdges: List[List[int]]) -> List[int]:
        redgraph=defaultdict(list)
        for i,j in redEdges:
            redgraph[i].append(j)
        bluegraph=defaultdict(list)
        for i,j in blueEdges:
            bluegraph[i].append(j)
        que=collections.deque()
        ans=[float("inf")]*n
        que.append((0,0,0))
        que.append((0,1,0))
        seen=set()
        seen.add((0,0))
        seen.add((0,1))
        while que:
            node,color,step=que.popleft()
            ans[node]=min(ans[node],step)
            if color==0:
                for i in redgraph[node]:
                    if (i,1-color) not in seen:
                        que.append((i,1,step+1))
                        seen.add((i,1-color))
            else:
                for i in bluegraph[node]:
                    if (i,1-color) not in seen:
                        que.append((i,0,step+1))
                        seen.add((i,1-color))
        return [x if x!=float("inf") else -1 for x in ans]
