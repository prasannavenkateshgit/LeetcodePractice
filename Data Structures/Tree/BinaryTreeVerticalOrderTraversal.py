'''
Given the root of a binary tree, return the vertical order traversal of its nodes' values. (i.e., from top to bottom, column by column).

If two nodes are in the same row and column, the order should be from left to right.
'''
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def verticalOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        dic=collections.defaultdict(list)
        q=collections.deque([(0,root)])
        ans=[]
        minx=float("inf")
        maxx=float("-inf")
        while q:
            x,node=q.popleft()
            dic[x].append(node.val)
            if x<minx:
                minx=x
            if x>maxx:
                maxx=x
            if node.left:
                q.append((x-1,node.left))
            if node.right:
                q.append((x+1,node.right))
        for i in range(minx,maxx+1,1):
            ans.append(dic[i])
        return ans
        
