'''
Given an integer array nums, move all 0's to the end of it while maintaining the relative order of the non-zero elements.

Note that you must do this in-place without making a copy of the array.
'''
class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        zptr=0
        i=0
        if 0 not in nums:
            return nums
        while i<len(nums):
            if nums[i]!=0:
                temp=nums[zptr]
                nums[zptr]=nums[i]
                nums[i]=temp
                zptr+=1
            i+=1
