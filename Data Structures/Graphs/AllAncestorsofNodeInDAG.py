'''
You are given a positive integer n representing the number of nodes of a Directed Acyclic Graph (DAG). The nodes are numbered from 0 to n - 1 (inclusive).

You are also given a 2D integer array edges, where edges[i] = [fromi, toi] denotes that there is a unidirectional edge from fromi to toi in the graph.

Return a list answer, where answer[i] is the list of ancestors of the ith node, sorted in ascending order.

A node u is an ancestor of another node v if u can reach v via a set of edges.
'''
class Solution:
    def getAncestors(self, n: int, edges: List[List[int]]) -> List[List[int]]:
        graph=defaultdict(list)
        for i,j in edges:
            graph[j].append(i)
        ans=[]
        for i in range(n):
            q=deque([i])
            seen=set()
            anc=[]
            while q:
                node=q.popleft()
                for j in graph[node]:
                    if j not in seen:
                        seen.add(j)
                        anc.append(j)
                        q.append(j)
            ans.append(sorted(anc))
        return ans
