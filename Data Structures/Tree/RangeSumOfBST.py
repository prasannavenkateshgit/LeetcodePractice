'''
Given the root node of a binary search tree and two integers low and high, return the sum of values of all nodes with a value in the inclusive range [low, high].
'''
import collections
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        if not root:
            return 0
        self.answer=0
        def dfs(node):
            if not node:
                return 0
            if node.val<=high and node.val>=low:
                self.answer+=node.val
            if node.val<low:
                dfs(node.right)
            elif node.val>high:
                dfs(node.left)
            else:
                dfs(node.left)
                dfs(node.right)
        dfs(root)
        return self.answer

        
