'''
You are given an integer array nums and an integer k. You may partition nums into one or more subsequences such that each element in nums appears in exactly one of the subsequences.

Return the minimum number of subsequences needed such that the difference between the maximum and minimum values in each subsequence is at most k.

A subsequence is a sequence that can be derived from another sequence by deleting some or no elements without changing the order of the remaining elements.
'''
class Solution:
    def partitionArray(self, nums: List[int], k: int) -> int:
        nums.sort()
        ans=1
        x=nums[0]
        for i in range(1,len(nums)):
            if nums[i]-x>k:
                x=nums[i]
                ans+=1
        return ans
