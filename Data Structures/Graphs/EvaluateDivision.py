'''
You are given an array of variable pairs equations and an array of real numbers values, where equations[i] = [Ai, Bi] and values[i] represent the equation Ai / Bi = values[i]. Each Ai or Bi is a string that represents a single variable.

You are also given some queries, where queries[j] = [Cj, Dj] represents the jth query where you must find the answer for Cj / Dj = ?.

Return the answers to all queries. If a single answer cannot be determined, return -1.0.

Note: The input is always valid. You may assume that evaluating the queries will not result in division by zero and that there is no contradiction.

Note: The variables that do not occur in the list of equations are undefined, so the answer cannot be determined for them.
'''
class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        def answer(start,end):
            if start not in graph:
                return -1
            seen={start}
            stack=[(start,1)]

            while stack:
                node,ratio=stack.pop()
                if node==end:
                    return ratio
                for neighbor in graph[node]:
                    if neighbor not in seen:
                        seen.add(neighbor)
                        stack.append((neighbor,ratio*graph[node][neighbor]))
            return -1
        
        graph=defaultdict(dict)
        for i in range(len(equations)):
            n,d=equations[i]
            val=values[i]
            graph[n][d]=val
            graph[d][n]=1/val

        ans=[]
        for n,d in queries:
            ans.append(answer(n,d))
        return ans
