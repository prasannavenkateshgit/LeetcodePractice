import math
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        counts=dict()
        for i in nums:
            if i in counts:
                counts[i]+=1
            else:
                counts[i]=1
        for j in counts:
            if counts[j]>math.floor(len(nums)/2):
                return j

##Another better method, Boyer Moore Voting Algorithm below. It uses O(n) time and O(1) space.
class Solution:
    def majorityElement(self, nums):
        count = 0
        candidate = None

        for num in nums:
            if count == 0:
                candidate = num
            count += (1 if num == candidate else -1)

        return candidate
