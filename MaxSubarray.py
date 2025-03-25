'''
Given an integer array nums, find the subarray with the largest sum, and return its sum.
'''
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        maxSub=nums[0]
        currsum=0
        for n in nums:
            if currsum<0:
                currsum=0
            currsum+=n
            maxSub=max(maxSub,currsum)
        return maxSub
        
