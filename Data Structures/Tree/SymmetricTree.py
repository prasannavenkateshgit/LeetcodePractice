'''
Given the root of a binary tree, check whether it is a mirror of itself (i.e., symmetric around its center).
'''
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        def mirror(n1,n2):
            if not n1 and not n2:
                return True
            if not n1 or not n2:
                return False
            return n1.val == n2.val and mirror(n1.left, n2.right) and mirror(n1.right,n2.left)
        return mirror(root.left,root.right)
