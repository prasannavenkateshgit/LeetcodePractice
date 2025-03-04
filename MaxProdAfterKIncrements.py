'''
You are given an array of non-negative integers nums and an integer k. In one operation, you may choose any element from nums and increment it by 1.

Return the maximum product of nums after at most k operations. Since the answer may be very large, return it modulo 109 + 7. Note that you should maximize the product before taking the modulo
'''
from heapq import *
class Solution:
    def maximumProduct(self, nums: List[int], k: int) -> int:
        MOD=10**9+7
        heapify(nums)
        for i in range(k):
            new=heappop(nums)
            heappush(nums,new+1)
        ans=1
        for x in nums:
            ans=(ans*x)%MOD
        return ans 
