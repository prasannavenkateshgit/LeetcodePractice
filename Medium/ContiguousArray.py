'''
Given a binary array nums, return the maximum length of a contiguous subarray with an equal number of 0 and 1.

 

Example 1:

Input: nums = [0,1]
Output: 2
Explanation: [0, 1] is the longest contiguous subarray with an equal number of 0 and 1.
Example 2:

Input: nums = [0,1,0]
Output: 2
Explanation: [0, 1] (or [1, 0]) is a longest contiguous subarray with equal number of 0 and 1.
'''
class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        counts={}
        counts[0]=-1
        curr = 0
        i=0
        maxlen=0
        for i in range(len(nums)):
            if nums[i]==1:
                curr+=1
            else:
                curr-=1
            if curr in counts:
                maxlen = max(maxlen, i-counts[curr])
            else:
                counts[curr]=i
        return maxlen
