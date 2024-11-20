'''
You are given a 0-indexed array nums consisting of positive integers. You can choose two indices i and j, such that i != j, and the sum of digits of the number nums[i] is equal to that of nums[j].

Return the maximum value of nums[i] + nums[j] that you can obtain over all possible indices i and j that satisfy the conditions.

 

Example 1:

Input: nums = [18,43,36,13,7]
Output: 54
Explanation: The pairs (i, j) that satisfy the conditions are:
- (0, 2), both numbers have a sum of digits equal to 9, and their sum is 18 + 36 = 54.
- (1, 4), both numbers have a sum of digits equal to 7, and their sum is 43 + 7 = 50.
So the maximum sum that we can obtain is 54.
Example 2:

Input: nums = [10,12,19,14]
Output: -1
Explanation: There are no two numbers that satisfy the conditions, so we return -1.
'''
import math
class Solution:
    def maximumSum(self, nums: List[int]) -> int:
        counts={}
        ans=0
        for i in nums:
            copy=i
            digisum=0
            while copy:
                digisum+=copy%10
                copy //=10
            if digisum in counts:
                ans=max(ans,i+counts[digisum])
                if counts[digisum]<i:
                    counts[digisum]=i
            else:
                counts[digisum]=i
        if ans==0:
            return -1
        return ans
