# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        traverse=[]
        stack=[root]
        visit=[False]
        cur=root
        while stack:
            cur=stack.pop()
            v=visit.pop()
            if cur:
                if v:
                    traverse.append(cur.val)
                else:
                    stack.append(cur.right)
                    visit.append(False)
                    stack.append(cur)
                    visit.append(True)
                    stack.append(cur.left)
                    visit.append(False)
        return traverse
