'''
You are given the root node of a binary search tree (BST) and a value to insert into the tree. Return the root node of the BST after the insertion. It is guaranteed that the new value does not exist in the original BST.

Notice that there may exist multiple valid ways for the insertion, as long as the tree remains a BST after insertion. You can return any of them.
'''
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        if not root:
            root=TreeNode(val)
            return root
        curr=root
        while 1:
            if not curr:
                break
            if curr and curr.val<val:
                if curr.right:
                    curr=curr.right
                else:
                    temp=TreeNode(val)
                    curr.right=temp
                    break
            if curr and curr.val>val:
                if curr.left:
                    curr=curr.left
                else:
                    temp=TreeNode(val)
                    curr.left=temp
                    break
        return root
