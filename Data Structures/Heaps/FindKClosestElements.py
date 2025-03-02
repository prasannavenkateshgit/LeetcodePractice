'''
Given a sorted integer array arr, two integers k and x, return the k closest integers to x in the array. The result should also be sorted in ascending order.

An integer a is closer to x than an integer b if:

|a - x| < |b - x|, or
|a - x| == |b - x| and a < b
'''
from heapq import *
class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        # heap=[(abs(x-i),i) for i in arr]
        # heapify(heap)
        # ans=[]
        # for j in range(k):
        #     val=heappop(heap)[1]
        #     ans.append(val)
        # return sorted(ans)
        q = collections.deque(arr)

        while len(q) > k:
            if abs(x - q[-1]) < abs(x - q[0]):
                q.popleft()
            else:
                q.pop()

        return list(q)

        
