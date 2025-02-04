'''
Given the root of a binary tree, return the zigzag level order traversal of its nodes' values. (i.e., from left to right, then right to left for the next level and alternate between).
'''
import collections
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        que=collections.deque([root])
        zig=0
        ans=[]
        if not root:
            return ans
        while que:
            curr=len(que)
            temp=[]
            for i in range(curr):
                node=que.popleft()
                if node:
                    temp.append(node.val)
                if node and node.left:
                    que.append(node.left)
                if node and node.right:
                    que.append(node.right)
            if zig%2!=0:
                temp=temp[::-1]
            ans.append(temp)
            zig+=1
        return ans

        
