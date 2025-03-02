'''
Given an array of points where points[i] = [xi, yi] represents a point on the X-Y plane and an integer k, return the k closest points to the origin (0, 0).

The distance between two points on the X-Y plane is the Euclidean distance (i.e., √(x1 - x2)2 + (y1 - y2)2).

You may return the answer in any order. The answer is guaranteed to be unique (except for the order that it is in).
'''
from heapq import *
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        distances=collections.defaultdict(list)
        heap=[]
        for i,j in points:
            dist=sqrt((i-0)**2+(j-0)**2)
            distances[dist].append([i,j])
            heappush(heap,-1*dist)
            if len(heap)>k:
                val=-1*heappop(heap)
                distances[val].pop()
        ans=[]
        for i in set(heap):
            ans+=(distances[-i])
        return ans
