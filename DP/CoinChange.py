'''
You are given an integer array coins representing coins of different denominations and an integer amount representing a total amount of money.

Return the fewest number of coins that you need to make up that amount. If that amount of money cannot be made up by any combination of the coins, return -1.

You may assume that you have an infinite number of each kind of coin.

 

Example 1:

Input: coins = [1,2,5], amount = 11
Output: 3
Explanation: 11 = 5 + 5 + 1
Example 2:

Input: coins = [2], amount = 3
Output: -1
Example 3:

Input: coins = [1], amount = 0
Output: 0
'''
class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        # n=amount+1
        # dp=[amount+1]*n
        # dp[0]=0
        # for i in range(1,n):
        #     for j in coins:
        #         if i-j>=0:
        #             dp[i]=min(dp[i],dp[i-j]+1)
        # if dp[amount]==amount+1:
        #     return -1
        # else:
        #     return dp[amount]
        def dp(i):
            if i<=0:
                return 0
            if i in memo:
                return memo[i]
            ans=amount+1
            for j in coins:
                if i-j>=0:
                    ans=min(ans,dp(i-j)+1)
            memo[i]=ans
            return memo[i]
        memo={}
        ans=dp(amount)
        return ans if ans!= amount+1 else -1
