'''
Given an array of integers arr and an integer k. Find the least number of unique integers after removing exactly k elements.
'''
from heapq import *
class Solution:
    def findLeastNumOfUniqueInts(self, arr: List[int], k: int) -> int:
        counts=defaultdict(int)
        for i in arr:
            counts[i]+=1
        heap=[]
        for key,val in counts.items():
            heappush(heap,(val,key))
        for i in range(k):
            val,key=heappop(heap)
            if val>1:
                val-=1
                heappush(heap,(val,key))
        ans=set()
        print(heap)
        for j in heap:
            ans.add(j[1])
        return len(ans)
