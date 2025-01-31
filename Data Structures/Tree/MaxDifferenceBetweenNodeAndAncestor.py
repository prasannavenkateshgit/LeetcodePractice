'''
Given the root of a binary tree, find the maximum value v for which there exist different nodes a and b where v = |a.val - b.val| and a is an ancestor of b.

A node a is an ancestor of b if either: any child of a is equal to b or any child of a is an ancestor of b.
'''
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxAncestorDiff(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        self.result = 0

        def helper(node,currmax,currmin):
            if not node:
                return
            self.result = max(self.result,abs(currmax-node.val),abs(currmin-node.val))
            currmax = max(currmax,node.val)
            currmin = min(currmin,node.val)
            helper(node.left,currmax,currmin)
            helper(node.right,currmax,currmin)
        helper(root,root.val,root.val)
        return self.result
