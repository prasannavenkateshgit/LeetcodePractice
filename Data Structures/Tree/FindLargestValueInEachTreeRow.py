'''
Given the root of a binary tree, return an array of the largest value in each row of the tree (0-indexed).
'''
import collections
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def largestValues(self, root: Optional[TreeNode]) -> List[int]:
        ans=[]
        que=collections.deque([root])
        if not root:
            return ans
        while que:
            curr=len(que)
            currmax=float("-infinity")
            for i in range(curr):
                if que[i] and que[i].val>currmax:
                    currmax=que[i].val
            ans.append(currmax)
            for j in range(curr):
                node=que.popleft()
                if node and node.left:
                    que.append(node.left)
                if node and node.right:
                    que.append(node.right)
        return ans
        
