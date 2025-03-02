'''
Given an integer array nums and an integer k, return the k most frequent elements. You may return the answer in any order.
'''
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        dic=collections.defaultdict(int)
        for i in nums:
            dic[i]+=1
        reverse=collections.defaultdict(list)
        for key,v in dic.items():
            reverse[v].append(key)
        heap=list(dic.values())
        heap=[-h for h in heap]
        heapify(heap)
        ans=[]
        if k==1:
            val=-1*heappop(heap)
            return [reverse[val].pop()]
        for j in range(k):
            val=-1*heappop(heap)
            ans.append(reverse[val].pop())
        return ans
