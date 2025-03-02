'''
You are given an integer array arr. You can choose a set of integers and remove all the occurrences of these integers in the array.

Return the minimum size of the set so that at least half of the integers of the array are removed.
'''
from heapq import *
class Solution:
    def minSetSize(self, arr: List[int]) -> int:
        dic=defaultdict(int)
        for i in arr:
            dic[i]+=1
        heap=[]
        for key,val in dic.items():
            heappush(heap,(-val,key))
        lenarr=len(arr)
        lenset=0
        ans=0
        while heap:
            ans+=1
            val,key=-heap[0][0],heap[0][1]
            lenset+=val
            if lenset>=lenarr//2:
                return ans
            heappop(heap)
        return ans
