'''
Given an array of integers nums, you start with an initial positive value startValue.

In each iteration, you calculate the step by step sum of startValue plus elements in nums (from left to right).

Return the minimum positive value of startValue such that the step by step sum is never less than 1.
'''
class Solution:
    def minStartValue(self, nums: List[int]) -> int:
        prefix = [nums[0]]
        i=1
        while i<len(nums):
            prefix.append(nums[i]+prefix[i-1])
            i+=1
        minprefix = 0
        for i in prefix:
            if i<minprefix:
                minprefix = i
        if minprefix<0:
            return (minprefix*-1)+1
        else:
            return 1
