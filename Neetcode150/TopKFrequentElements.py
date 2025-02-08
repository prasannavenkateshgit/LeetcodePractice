'''
Given an integer array nums and an integer k, return the k most frequent elements within the array.

The test cases are generated such that the answer is always unique.

You may return the output in any order.
'''
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        dic=defaultdict(int)
        maxval=0
        for i in nums:
            dic[i]+=1
        most=[[] for i in range(len(nums)+1)]
        print(dic)
        for key,v in dic.items():
            most[v].append(key)
        ans=[]
        for i in range(len(most)-1,0,-1):
            for n in most[i]:
                ans.append(n)
                if len(ans)==k:
                    return ans
