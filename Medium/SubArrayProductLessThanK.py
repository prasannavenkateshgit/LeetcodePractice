'''
Given an array of integers nums and an integer k, return the number of contiguous subarrays where the product of all the elements in the subarray is strictly less than k.
'''
class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        # product = 1
        # left = 0
        # right = 0
        # count=0
        # i=0
        # while i<len(nums):
        #     product = nums[i]
        #     left = i
        #     right = left+1
        #     while product<k:
        #         count+=1
        #         if right<len(nums):
        #             product = product * nums[right]
        #             right +=1
        #         else:
        #             break
        #     i+=1
        # return count
      #This is a O(n^2) solution since we iteratively build the sliding window in each iteration, while the below is amortized O(n) since we only go into the second loop when product is bigger than k and prune left side.

        count = left = right = 0
        product = 1
        if k<=1:
            return count
        while right<len(nums):
            product = product * nums[right]
            while product>=k:
                product = product / nums[left]
                left+=1
            count+= 1+(right-left)
            right+=1
        return count
