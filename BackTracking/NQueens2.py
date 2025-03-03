'''
The n-queens puzzle is the problem of placing n queens on an n x n chessboard such that no two queens attack each other.

Given an integer n, return the number of distinct solutions to the n-queens puzzle.
'''
class Solution:
    def totalNQueens(self, n: int) -> int:
        cols=set()
        pos=set()
        neg=set()
        res=0

        def backtrack(r):
            if r==n:
                nonlocal res
                res+=1
                return
            for c in range(n):
                if c not in cols and (r+c) not in pos and (r-c) not in neg:
                    cols.add(c)
                    pos.add(r+c)
                    neg.add(r-c)
                    backtrack(r+1)
                    cols.remove(c)
                    pos.remove(r+c)
                    neg.remove(r-c)
        backtrack(0)
        return res
        
