'''
You are given a 0-indexed array of positive integers w where w[i] describes the weight of the ith index.

You need to implement the function pickIndex(), which randomly picks an index in the range [0, w.length - 1] (inclusive) and returns it. The probability of picking an index i is w[i] / sum(w).

For example, if w = [1, 3], the probability of picking index 0 is 1 / (1 + 3) = 0.25 (i.e., 25%), and the probability of picking index 1 is 3 / (1 + 3) = 0.75 (i.e., 75%).
'''
class Solution:

    def __init__(self, w: List[int]):
        self.cumsum=[]
        total=0
        for i in w:
            total+=i
            self.cumsum.append(total)
        self.total=total

    def pickIndex(self) -> int:
        pick=random.uniform(0,self.total)
        l=0
        r=len(self.cumsum)
        while l<r:
            mid=(l+r)//2
            if self.cumsum[mid]<pick:
                l=mid+1
            else:
                r=mid
        return l
        


# Your Solution object will be instantiated and called as such:
# obj = Solution(w)
# param_1 = obj.pickIndex()
