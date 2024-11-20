'''
Given an array of integers nums and an integer k, return the total number of subarrays whose sum equals to k.

A subarray is a contiguous non-empty sequence of elements within an array.
'''
from collections import defaultdict
class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        counts = defaultdict(int)
        counts[0]=1
        curr=0
        ans=0
        for i in nums:
            curr+=i
            ans+=counts[curr-k]
            counts[curr]+=1
        return ans
        
