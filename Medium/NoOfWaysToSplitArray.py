'''You are given a 0-indexed integer array nums of length n.

nums contains a valid split at index i if the following are true:

The sum of the first i + 1 elements is greater than or equal to the sum of the last n - i - 1 elements.
There is at least one element to the right of i. That is, 0 <= i < n - 1.
Return the number of valid splits in nums.'''

class Solution:
    def waysToSplitArray(self, nums: List[int]) -> int:
        n = len(nums)
        prefix = [nums[0]]
        reversednums = nums[::-1]
        i=1
        while i<len(nums):
            prefix.append(nums[i]+prefix[i-1])
            i+=1
        count=0
        k = 0
        while k<len(nums)-1:
            if prefix[k]>=prefix[n-1]-prefix[k]:
                count+=1
            k+=1
        return count
