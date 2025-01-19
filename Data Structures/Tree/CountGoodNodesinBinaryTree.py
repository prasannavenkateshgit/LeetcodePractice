'''
Given a binary tree root, a node X in the tree is named good if in the path from root to X there are no nodes with a value greater than X.

Return the number of good nodes in the binary tree.
'''
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        def dfs(node,maxyet):
            if not node:
                return 0
            left=dfs(node.left,max(maxyet,node.val))
            right=dfs(node.right,max(maxyet,node.val))
            ans=left+right
            if node.val>=maxyet:
                ans+=1
            return ans
        return dfs(root,float("-inf"))
