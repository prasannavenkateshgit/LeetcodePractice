'''
Given an m x n grid of characters board and a string word, return true if word exists in the grid.

The word can be constructed from letters of sequentially adjacent cells, where adjacent cells are horizontally or vertically neighboring. The same letter cell may not be used more than once.
'''
class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        def valid(row,col):
            return 0<=row<m and 0<=col<n
        m=len(board)
        n=len(board[0])
        found=0
        def backtrack(r,c,i,seen):
            if i==len(word):
                return True
            directions=[(1,0),(0,1),(-1,0),(0,-1)]
            for dx,dy in directions:
                nr,nc=r+dx,c+dy
                if valid(nr,nc) and (nr,nc) not in seen:
                    if board[nr][nc]==word[i]:
                        seen.add((nr,nc))
                        if backtrack(nr,nc,i+1,seen):
                            return True
                        seen.remove((nr,nc))
            return False
        for i in range(m):
            for j in range(n):
                if board[i][j]==word[0] and backtrack(i,j,1,{(i,j)}):
                    return True
        return False
