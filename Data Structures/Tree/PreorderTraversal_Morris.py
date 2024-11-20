# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        curr=root
        traversed=[]
        while curr:
            if not curr.left:
                traversed.append(curr.val)
                curr=curr.right
            else:
                last=curr.left
                while last.right and last.right!=curr:
                    last=last.right
                if not last.right:
                    traversed.append(curr.val)
                    last.right=curr
                    curr=curr.left
                else:
                    last.right=None
                    curr=curr.right
        return traversed
