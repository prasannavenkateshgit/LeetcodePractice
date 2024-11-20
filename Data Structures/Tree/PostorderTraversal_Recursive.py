# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        traverse=[]
        def visit(node):
            if not node:
                return
            visit(node.left)
            visit(node.right)
            traverse.append(node.val)
        visit(root)
        return traverse
