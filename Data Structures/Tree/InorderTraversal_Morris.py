# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        traverse=[]
        cur=root
        while cur:
            if not cur.left:
                traverse.append(cur.val)
                cur=cur.right
            else:
                rchild=cur.left
                while rchild.right:
                    rchild=rchild.right
                rchild.right=cur
                temp=cur
                cur=cur.left
                temp.left=None
        return traverse
