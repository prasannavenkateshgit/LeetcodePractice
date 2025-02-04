'''
Given the root of a binary tree, imagine yourself standing on the right side of it, return the values of the nodes you can see ordered from top to bottom.
'''
import collections
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        que=collections.deque([root])
        ans=[]
        while que:
            curr=len(que)
            temp=que[-1]
            if temp:
                ans.append(temp.val)
            for i in range(curr):
                node=que.popleft()
                if node and node.left:
                    que.append(node.left)
                if node and node.right:
                    que.append(node.right)   
        return ans
