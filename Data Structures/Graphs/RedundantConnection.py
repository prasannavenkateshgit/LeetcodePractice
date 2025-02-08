'''
In this problem, a tree is an undirected graph that is connected and has no cycles.

You are given a graph that started as a tree with n nodes labeled from 1 to n, with one additional edge added. The added edge has two different vertices chosen from 1 to n, and was not an edge that already existed. The graph is represented as an array edges of length n where edges[i] = [ai, bi] indicates that there is an edge between nodes ai and bi in the graph.

Return an edge that can be removed so that the resulting graph is a tree of n nodes. If there are multiple answers, return the answer that occurs last in the input.
'''
class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        n=len(edges)
        par=[i for i in range(n)]
        rank=[1]*n
        redundant=[]
        print(par)

        def find(n1):
            res=n1
            while res!=par[res]:
                par[res]=par[par[res]]
                res=par[res]
            return res

        def union(n1,n2):
            p1, p2 = find(n1), find(n2)
            if p1==p2:
                redundant.append([n1+1,n2+1])
            if rank[p1]>rank[p2]:
                par[p2]=p1
                rank[p1]+=rank[p2]
            else:
                par[p1]=p2
                rank[p2]+=rank[p1]
        
        for n1,n2 in edges:
            union(n1-1,n2-1)
        
        return redundant[-1]
