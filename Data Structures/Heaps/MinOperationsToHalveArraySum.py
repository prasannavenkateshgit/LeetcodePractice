'''
You are given an array nums of positive integers. In one operation, you can choose any number from nums and reduce it to exactly half the number. (Note that you may choose this reduced number in future operations.)

Return the minimum number of operations to reduce the sum of nums by at least half.
'''
from heapq import *
class Solution:
    def halveArray(self, nums: List[int]) -> int:
        target=sum(nums)/2
        heap=[-num for num in nums]
        heapq.heapify(heap)

        ans=0
        while target>0:
            maxelement=heappop(heap)/2
            ans+=1
            target+=maxelement
            heappush(heap,maxelement)
        return ans
