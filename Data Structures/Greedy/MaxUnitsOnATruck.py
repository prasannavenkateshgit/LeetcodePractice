'''
You are assigned to put some amount of boxes onto one truck. You are given a 2D array boxTypes, where boxTypes[i] = [numberOfBoxesi, numberOfUnitsPerBoxi]:

numberOfBoxesi is the number of boxes of type i.
numberOfUnitsPerBoxi is the number of units in each box of the type i.
You are also given an integer truckSize, which is the maximum number of boxes that can be put on the truck. You can choose any boxes to put on the truck as long as the number of boxes does not exceed truckSize.

Return the maximum total number of units that can be put on the truck.
'''
from heapq import *
class Solution:
    def maximumUnits(self, boxTypes: List[List[int]], truckSize: int) -> int:
        heap=[]
        for i in boxTypes:
            heappush(heap,(-i[1],i[0]))
        ans=0
        ans
        while truckSize>0:
            if heap:
                cont,box=-heap[0][0],heap[0][1]
                if truckSize-box>=0:
                    ans+=cont*box
                    truckSize-=box
                else:
                    ans+=cont*truckSize
                    truckSize-=box
                heappop(heap)
            else:
                break
        return ans
