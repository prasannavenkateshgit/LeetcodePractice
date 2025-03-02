'''
You are given an integer array nums of length n, and an integer array queries of length m.

Return an array answer of length m where answer[i] is the maximum size of a subsequence that you can take from nums such that the sum of its elements is less than or equal to queries[i].

A subsequence is an array that can be derived from another array by deleting some or no elements without changing the order of the remaining elements.
'''
class Solution:
    def answerQueries(self, nums: List[int], queries: List[int]) -> List[int]:
        # nums.sort()
        # ans=[]
        # for i in queries:
        #     count=0
        #     for num in nums:
        #         if i>=num:
        #             i-=num
        #             count+=1
        #         else:
        #             break
        #     ans.append(count)
        # return ans
        nums.sort()
        for i in range(1,len(nums)):
            nums[i]+=nums[i-1]
        ans=[]
        left=0
        right=len(nums)
        for i in queries:
            left=0
            right=len(nums)
            while left<right:
                mid=(left+right)//2
                if nums[mid]>i:
                    right=mid
                else:
                    left=mid+1
            ans.append(left)
        return ans
