'''
Given an integer array nums and an integer k, split nums into k non-empty subarrays such that the largest sum of any subarray is minimized.

Return the minimized largest sum of the split.

A subarray is a contiguous part of the array.
'''
class Solution:
    def splitArray(self, nums: List[int], k: int) -> int:
        def check(lar):
            count=0
            cursum=0
            for i in nums:
                cursum+=i
                if cursum>lar:
                    count+=1
                    cursum=i
            return count+1<=k
        l=max(nums)
        r=sum(nums)
        ans=r
        while l<=r:
            mid=l+((r-l)//2)
            if check(mid):
                ans=mid
                r=mid-1
            else:
                l=mid+1
        return ans
