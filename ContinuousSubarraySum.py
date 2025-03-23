'''
Given an integer array nums and an integer k, return true if nums has a good subarray or false otherwise.

A good subarray is a subarray where:

its length is at least two, and
the sum of the elements of the subarray is a multiple of k.
Note that:

A subarray is a contiguous part of the array.
An integer x is a multiple of k if there exists an integer n such that x = n * k. 0 is always a multiple of k.
'''
class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        rem={0:-1}
        total=0
        for i in range(len(nums)):
            total+=nums[i]
            r=total%k
            if r not in rem:
                rem[r]=i
            elif i-rem[r]>1:
                return True
        return False
        
