'''
Given the root of a binary tree, return the sum of values of its deepest leaves.
'''
import collections
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deepestLeavesSum(self, root: Optional[TreeNode]) -> int:
        que=collections.deque([root])
        ans=[]
        while que:
            curr=len(que)
            temp=[]
            for i in range(curr):
                node=que.popleft()
                temp.append(node.val)
                if node and node.left:
                    que.append(node.left)
                if node and node.right:
                    que.append(node.right)
            ans.append(temp)
        return sum(ans[-1])
