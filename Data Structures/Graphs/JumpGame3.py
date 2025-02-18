'''
Given an array of non-negative integers arr, you are initially positioned at start index of the array. When you are at index i, you can jump to i + arr[i] or i - arr[i], check if you can reach any index with value 0.

Notice that you can not jump outside of the array at any time.
'''
class Solution:
    def canReach(self, arr: List[int], start: int) -> bool:
        def valid(ni):
            return 0<=ni<n
        n=len(arr)
        q=collections.deque()
        q.append(start)
        if arr[start]==0:
            return True
        seen=set()
        seen.add(start)
        while q:
            i=q.popleft()
            left=i-arr[i]
            right=i+arr[i]
            if valid(left):
                if arr[left]==0:
                    return True
                if left not in seen:
                    seen.add(left)
                    q.append(left)
            if valid(right):
                if arr[right]==0:
                    return True
                if right not in seen:
                    seen.add(right)
                    q.append(right)
        return False
        
