'''
Given the root of a binary tree, the depth of each node is the shortest distance to the root.

Return the smallest subtree such that it contains all the deepest nodes in the original tree.

A node is called the deepest if it has the largest depth possible among any node in the entire tree.

The subtree of a node is a tree consisting of that node, plus the set of all descendants of that node.
'''
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def subtreeWithAllDeepest(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        def bfs(root):
            q=collections.deque([root])
            levels=[]
            level=0
            while q:
                curr=len(q)
                for i in range(curr):
                    levels.append([])
                    node=q.popleft()
                    levels[level].append(node)
                    if node and node.left:
                        q.append(node.left)
                    if node and node.right:
                        q.append(node.right)
                level+=1
            return levels

        def lca(root,p,q):
            if not root:
                return None
            if root==p or root==q:
                return root
            left=lca(root.left,p,q)
            right=lca(root.right,p,q)
            if left and right:
                return root
            if left:
                return left
            if right:
                return right
        deepest=bfs(root)
        for i in deepest:
            if i !=[]:
                last=i
        return lca(root,last[0],last[-1])
