'''
Given an array of strings words and an integer k, return the k most frequent strings.

Return the answer sorted by the frequency from highest to lowest. Sort the words with the same frequency by their lexicographical order.
'''
from heapq import *
class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        dic=defaultdict(int)
        reverse=defaultdict(list)
        minheap=[]
        for i in words:
            dic[i]+=1
        for key,v in dic.items():
            reverse[v].append(key)
            heappush(minheap,-v)

        ans=[]
        for i in range(k):
            temp=heappop(minheap)
            temp2=reverse[-temp]
            if temp2:
                temp2.sort()
                for j in temp2:
                    ans.append(j)
                    if len(ans)>=k:
                        return ans
            reverse.pop(-temp)
        return ans

#Time Complexity: O(N * log(K))
#Space Complexity: O(N)
