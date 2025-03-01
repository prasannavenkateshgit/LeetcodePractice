'''
The median is the middle value in an ordered integer list. If the size of the list is even, there is no middle value. So the median is the mean of the two middle values.

For examples, if arr = [2,3,4], the median is 3.
For examples, if arr = [1,2,3,4], the median is (2 + 3) / 2 = 2.5.
You are given an integer array nums and an integer k. There is a sliding window of size k which is moving from the very left of the array to the very right. You can only see the k numbers in the window. Each time the sliding window moves right by one position.

Return the median array for each window in the original array. Answers within 10-5 of the actual value will be accepted.
'''
from heapq import *
class Solution:
    def medianSlidingWindow(self, nums: List[int], k: int) -> List[float]:
        maxheap=[]
        minheap=[]
        heapdict=collections.defaultdict(int)

        res = []
        for i in range(k):
            heappush(maxheap,-nums[i])
            heappush(minheap,-heappop(maxheap))
            if len(minheap)>len(maxheap):
                heappush(maxheap,-heappop(minheap))
        if k%2==1:
            median=-maxheap[0]
            res.append(median)
        else:
            median=(-maxheap[0]+minheap[0])/2
            res.append(median)
        
        for i in range(k,len(nums)):
            prev=nums[i-k]
            heapdict[prev]+=1
            balance=-1 if prev<=median else 1
            if nums[i]<=median:
                balance+=1
                heappush(maxheap,-nums[i])
            else:
                balance-=1
                heappush(minheap,nums[i])
            if balance<0:
                heappush(maxheap,-heappop(minheap))
            elif balance>0:
                heappush(minheap,-heappop(maxheap))
            while maxheap and heapdict[-maxheap[0]]>0:
                heapdict[-maxheap[0]]-=1
                heappop(maxheap)
            while minheap and heapdict[minheap[0]]>0:
                heapdict[minheap[0]]-=1
                heappop(minheap)
            if k%2==1:
                median=-maxheap[0]
                res.append(median)
            else:
                median=(-maxheap[0]+minheap[0])/2
                res.append(median)
        return res
            
        
