'''
A binary tree is named Even-Odd if it meets the following conditions:

The root of the binary tree is at level index 0, its children are at level index 1, their children are at level index 2, etc.
For every even-indexed level, all nodes at the level have odd integer values in strictly increasing order (from left to right).
For every odd-indexed level, all nodes at the level have even integer values in strictly decreasing order (from left to right).
Given the root of a binary tree, return true if the binary tree is Even-Odd, otherwise return false.
'''
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isEvenOddTree(self, root: Optional[TreeNode]) -> bool:
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
        print(ans)
        for i in range(len(ans)):
            if i%2==0:
                j=0
                while j<len(ans[i]):
                    if ans[i][j]%2!=1:
                        return False
                    if j+1<len(ans[i]):
                        if ans[i][j]>=ans[i][j+1]:
                            return False
                    j+=1
            else:
                j=0
                while j<len(ans[i]):
                    if ans[i][j]%2!=0:
                        return False
                    if j+1<len(ans[i]):
                        if ans[i][j]<=ans[i][j+1]:
                            return False
                    j+=1
        return True
        
