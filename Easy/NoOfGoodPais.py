'''
Given an array of integers nums, return the number of good pairs.

A pair (i, j) is called good if nums[i] == nums[j] and i < j.
'''
class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        h={}

        count=0

        for i in nums:
            if i in h:
                count += h[i]
                h[i]+=1
            else:
                h[i]=1

        return count
