'''
Given two binary search trees root1 and root2, return a list containing all the integers from both trees sorted in ascending order.
'''
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getAllElements(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> List[int]:
        def dfs(root,path):
            if not root:
                return
            dfs(root.left,path)
            path.append(root.val)
            dfs(root.right,path)
        self.path1=[]
        self.path2=[]
        dfs(root1,self.path1)
        dfs(root2,self.path2)
        print(self.path1)
        print(self.path2)
        res=[]
        i=0
        j=0
        while i<len(self.path1) and j<len(self.path2):
            if self.path1[i]<self.path2[j]:
                res.append(self.path1[i])
                i+=1
            else:
                res.append(self.path2[j])
                j+=1
        while i<len(self.path1):
            res.append(self.path1[i])
            i+=1
        while j<len(self.path2):
            res.append(self.path2[j])
            j+=1
        return res

        
