'''
Given the root of a binary tree and an integer targetSum, return true if the tree has a root-to-leaf path such that adding up all the values along the path equals targetSum.

A leaf is a node with no children.
'''
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        def dfs(node,treesum):
            if not node:
                return False
            
            if node.left==None and node.right==None:
                return treesum+node.val == targetSum
            treesum+=node.val
            left = dfs(node.left,treesum)
            right = dfs(node.right, treesum)
            return left or right
        return dfs(root,0)
