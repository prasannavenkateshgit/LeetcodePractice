'''
You are given an integer array prices where prices[i] is the price of NeetCoin on the ith day.

You may choose a single day to buy one NeetCoin and choose a different day in the future to sell it.

Return the maximum profit you can achieve. You may choose to not make any transactions, in which case the profit would be 0.
'''
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l=0
        r=l+1
        price=0
        while r<len(prices):
            if prices[r]-prices[l]>price:
                price=prices[r]-prices[l]
            if prices[r]<prices[l]:
                l=r
            r+=1
        return price
