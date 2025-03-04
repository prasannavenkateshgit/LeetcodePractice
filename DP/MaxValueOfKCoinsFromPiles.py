'''
There are n piles of coins on a table. Each pile consists of a positive number of coins of assorted denominations.

In one move, you can choose any coin on top of any pile, remove it, and add it to your wallet.

Given a list piles, where piles[i] is a list of integers denoting the composition of the ith pile from top to bottom, and a positive integer k, return the maximum total value of coins you can have in your wallet if you choose exactly k coins optimally.
'''
class Solution:
    def maxValueOfCoins(self, piles: List[List[int]], k: int) -> int:
        n=len(piles)
        memo=[[-1]*(k+1) for _ in range(n)]
        def dp(i,coins):
            if i==n:
                return 0
            if memo[i][coins]!=-1:
                return memo[i][coins]
            memo[i][coins]=dp(i+1,coins)
            curr=0
            for j in range(min(coins,len(piles[i]))):
                curr+=piles[i][j]
                memo[i][coins]=max(memo[i][coins],curr+dp(i+1,coins-j-1))
            return memo[i][coins]
        return dp(0,k)
