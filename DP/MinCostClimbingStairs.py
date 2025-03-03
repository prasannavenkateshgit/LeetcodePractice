'''
You are given an integer array cost where cost[i] is the cost of ith step on a staircase. Once you pay the cost, you can either climb one or two steps.

You can either start from the step with index 0, or the step with index 1.

Return the minimum cost to reach the top of the floor
'''
class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        def dp(i):
            if i<=1:
                return 0
            if i in memo:
                return memo[i]
            memo[i]=min(dp(i-1)+cost[i-1],dp(i-2)+cost[i-2])
            return memo[i]
        memo={}
        return dp(len(cost))
