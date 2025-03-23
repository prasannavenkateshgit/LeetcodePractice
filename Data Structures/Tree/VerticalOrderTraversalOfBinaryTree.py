'''
Given the root of a binary tree, calculate the vertical order traversal of the binary tree.

For each node at position (row, col), its left and right children will be at positions (row + 1, col - 1) and (row + 1, col + 1) respectively. The root of the tree is at (0, 0).

The vertical order traversal of a binary tree is a list of top-to-bottom orderings for each column index starting from the leftmost column and ending on the rightmost column. There may be multiple nodes in the same row and same column. In such a case, sort these nodes by their values.

Return the vertical order traversal of the binary tree.
'''
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def verticalTraversal(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        q=collections.deque([(root,0,0)])
        dic=collections.defaultdict(list)
        minx=float("inf")
        maxx=float("-inf")
        while q:
            temp=[]
            for _ in range(len(q)):
                node,row,col=q.popleft()
                dic[(row,col)].append(node.val)
                minx=min(minx,col)
                maxx=max(maxx,col)
                temp.append(node.val)
                if node.left:
                    q.append((node.left,row+1,col-1))
                if node.right:
                    q.append((node.right,row+1,col+1))
        ans=[]
        for j in range(minx,maxx+1,1):
            temp=[]
            for i in range(row+1):
                temp2=dic[(i,j)]
                temp2.sort()
                temp+=temp2
            if temp:
                ans.append(temp)
        return ans
