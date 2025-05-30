'''
You are given an array of integers nums and an integer k. There is a sliding window of size k that starts at the left edge of the array. The window slides one position to the right until it reaches the right edge of the array.

Return a list that contains the maximum element in the window at each step.
'''
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        out=[]
        q=deque()
        l=r=0
        while r<len(nums):
            while q and nums[q[-1]]<nums[r]:
                q.pop()
            q.append(r)
            if l>q[0]:
                q.popleft()
            if (r+1)>=k:
                out.append(nums[q[0]])
                l+=1
            r+=1
        return out
