'''
There is an infrastructure of n cities with some number of roads connecting these cities. Each roads[i] = [ai, bi] indicates that there is a bidirectional road between cities ai and bi.

The network rank of two different cities is defined as the total number of directly connected roads to either city. If a road is directly connected to both cities, it is only counted once.

The maximal network rank of the infrastructure is the maximum network rank of all pairs of different cities.

Given the integer n and the array roads, return the maximal network rank of the entire infrastructure.
'''
class Solution:
    def maximalNetworkRank(self, n: int, roads: List[List[int]]) -> int:
        graph=defaultdict(set)
        for i,j in roads:
            graph[i].add(j)
            graph[j].add(i)
        maxrank=0
        i=0
        while i<n:
            j=i+1
            while j<n:
                hasconn=1 if i in graph[j] else 0
                city1=len(graph[i])
                city2=len(graph[j])
                maxrank=max(maxrank,city1+city2-hasconn)
                j+=1
            i+=1
        return maxrank
