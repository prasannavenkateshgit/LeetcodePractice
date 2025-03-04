'''
You are given an integer array prices where prices[i] is the price of a given stock on the ith day, and an integer k.

Find the maximum profit you can achieve. You may complete at most k transactions: i.e. you may buy at most k times and sell at most k times.

Note: You may not engage in multiple transactions simultaneously (i.e., you must sell the stock before you buy again).
'''
class Solution:
    def maxProfit(self, k: int, prices: List[int]) -> int:
        n=len(prices)
        memo=[[[0]*(k+1) for _ in range(2)] for _ in range(len(prices)+1)]
        # def dp(i,holding,remain):
        #     if i==len(prices) or remain==0:
        #         return memo[i][holding][remain]
        #     ans=dp(i+1,holding,remain)
        #     if holding:
        #         ans=max(ans,prices[i]+dp(i+1,0,remain-1))
        #     else:
        #         ans=max(ans,-prices[i]+dp(i+1,1,remain))
        #     memo[i][holding][remain]=ans
        #     return memo[i][holding][remain]
        # return dp(0,0,k)
        for i in range(n-1,-1,-1):
            for remain in range(1,k+1):
                for holding in range(2):
                    ans=memo[i+1][holding][remain]
                    if holding:
                        ans=max(ans,prices[i]+memo[i+1][0][remain-1])
                    else:
                        ans=max(ans,-prices[i]+memo[i+1][1][remain])
                    memo[i][holding][remain]=ans
        return memo[0][0][k]
