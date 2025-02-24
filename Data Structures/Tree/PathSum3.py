'''
Given the root of a binary tree and an integer targetSum, return the number of paths where the sum of the values along the path equals targetSum.

The path does not need to start or end at the root or a leaf, but it must go downwards (i.e., traveling only from parent nodes to child nodes).
'''
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        prefix={0:1}

        def dfs(node,currsum):
            if not node:
                return 0
            currsum+=node.val
            numpaths = prefix.get(currsum-targetSum,0)
            prefix[currsum]=prefix.get(currsum,0)+1
            numpaths+=dfs(node.left, currsum)
            numpaths+=dfs(node.right, currsum)
            prefix[currsum]-=1
            return numpaths
        return dfs(root,0)
        
