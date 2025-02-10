'''
Given the root of a binary tree, the value of a target node target, and an integer k, return an array of the values of all nodes that have a distance k from the target node.

You can return the answer in any order.
'''
import collections
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def distanceK(self, root: TreeNode, target: TreeNode, k: int) -> List[int]:
        def dfs(node,parent):
            if not node:
                return
            node.parent = parent
            dfs(node.left,node)
            dfs(node.right,node)
        dfs(root,None)

        que = collections.deque([target])
        seen=set()
        seen.add(target)
        count=0
        while que and count<k:
            curr=len(que)
            for i in range(curr):
                node=que.popleft()
                if node.left and node.left not in seen:
                    seen.add(node.left)
                    que.append(node.left)
                if node.right and node.right not in seen:
                    seen.add(node.right)
                    que.append(node.right)
                if node.parent and node.parent not in seen:
                    seen.add(node.parent)
                    que.append(node.parent)
            count+=1
        return [node.val for node in que]
        
