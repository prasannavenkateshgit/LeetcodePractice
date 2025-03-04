'''

You are given an array prices where prices[i] is the price of a given stock on the ith day.

Find the maximum profit you can achieve. You may complete as many transactions as you like (i.e., buy one and sell one share of the stock multiple times) with the following restrictions:

After you sell your stock, you cannot buy stock on the next day (i.e., cooldown one day).
Note: You may not engage in multiple transactions simultaneously (i.e., you must sell the stock before you buy again).
'''
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        def dp(i,buy):
            if i>=len(prices):
                return 0
            if (i,buy) in memo:
                return memo[(i,buy)]
            skip=dp(i+1,buy)
            if buy:
                memo[(i,buy)]=max(skip,-prices[i]+dp(i+1, not buy))
            else:
                memo[(i,buy)]=max(skip,prices[i]+dp(i+2, not buy))
            return memo[(i,buy)]
        memo={}
        return dp(0,True)
