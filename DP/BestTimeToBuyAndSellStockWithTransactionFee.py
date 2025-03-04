'''
You are given an array prices where prices[i] is the price of a given stock on the ith day, and an integer fee representing a transaction fee.

Find the maximum profit you can achieve. You may complete as many transactions as you like, but you need to pay the transaction fee for each transaction.

Note:

You may not engage in multiple transactions simultaneously (i.e., you must sell the stock before you buy again).
The transaction fee is only charged once for each stock purchase and sale.
'''
class Solution:
    def maxProfit(self, prices: List[int], fee: int) -> int:
        def dp(i,holding):
            if i>=len(prices):
                return 0
            if (i,holding) in memo:
                return memo[(i,holding)]
            ans=dp(i+1,holding)
            if holding:
                ans=max(dp(i+1,holding),prices[i]-fee+dp(i+1,0))
            else:
                ans=max(dp(i+1,holding),-prices[i]+dp(i+1,1))
            memo[(i,holding)]=ans
            return memo[(i,holding)]
        memo={}
        return dp(0,0)
