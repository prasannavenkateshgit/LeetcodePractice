'''

You are given a 0-indexed array nums of n integers, and an integer k.

The k-radius average for a subarray of nums centered at some index i with the radius k is the average of all elements in nums between the indices i - k and i + k (inclusive). If there are less than k elements before or after the index i, then the k-radius average is -1.

Build and return an array avgs of length n where avgs[i] is the k-radius average for the subarray centered at index i.

The average of x elements is the sum of the x elements divided by x, using integer division. The integer division truncates toward zero, which means losing its fractional part.

For example, the average of four elements 2, 3, 1, and 5 is (2 + 3 + 1 + 5) / 4 = 11 / 4 = 2.75, which truncates to 2.
'''
import math
class Solution:
    def getAverages(self, nums: List[int], k: int) -> List[int]:
        prefix = [nums[0]]
        ans=[]
        i=1
        while i<len(nums):
            prefix.append(nums[i]+prefix[i-1])
            i+=1
        j=0
        while j<len(nums):
            if j-k<0 or j+k>=len(nums):
                ans.append(-1)
            else:
                avg1 = (prefix[j+k]-prefix[j-k]+nums[j-k])/((2*k)+1)
                avg1 = math.floor(avg1)
                ans.append(avg1)
            j+=1
        return ans
