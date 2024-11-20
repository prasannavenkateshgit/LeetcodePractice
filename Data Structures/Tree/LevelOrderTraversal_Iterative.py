from collections import deque
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        ans=[]
        if not root:
            return ans
        level=0
        queue=deque([root,])
        while queue:
            ans.append([])
            levellen=len(queue)
            for i in range(levellen):
                node=queue.popleft()
                ans[level].append(node.val)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            level+=1
        return ans
