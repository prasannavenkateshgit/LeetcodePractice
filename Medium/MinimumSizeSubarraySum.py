'''
Given an array of positive integers nums and a positive integer target, return the minimal length of a 
subarray
 whose sum is greater than or equal to target. If there is no such subarray, return 0 instead.'''
class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        ans=float('inf')
        left=0
        sum=0
        i=0
        while i<len(nums):
            sum=sum+nums[i]
            while sum>=target:
                ans=min(ans,i+1-left)
                sum=sum-nums[left]
                left=left+1
            i=i+1
        if ans==float('inf'):
            return 0
        else:
            return ans
