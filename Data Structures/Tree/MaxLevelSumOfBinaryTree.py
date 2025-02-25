'''
Given the root of a binary tree, the level of its root is 1, the level of its children is 2, and so on.

Return the smallest level x such that the sum of all the values of nodes at level x is maximal.
'''
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxLevelSum(self, root: Optional[TreeNode]) -> int:
        ans=[]
        q=collections.deque([root])
        while q:
            temp=[]
            for i in range(len(q)):
                node=q.popleft()
                if node:
                    temp.append(node.val)
                    if node.left:
                        q.append(node.left)
                    if node.right:
                        q.append(node.right)
            ans.append(temp)
        res=1
        maxlevel=float("-inf")
        print(ans)
        for i in range(len(ans)):
            if sum(ans[i])>maxlevel:
                maxlevel=sum(ans[i])
                print(sum(ans[i]))
                res=i+1
        return res
        
