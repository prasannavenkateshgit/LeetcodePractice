'''
Given an n x n array of integers matrix, return the minimum sum of any falling path through matrix.

A falling path starts at any element in the first row and chooses the element in the next row that is either directly below or diagonally left/right. Specifically, the next element from position (row, col) will be (row + 1, col - 1), (row + 1, col), or (row + 1, col + 1).
'''
class Solution:
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:
        def dp(r,c):
            if r==0:
                return matrix[r][c]
            if (r,c) in memo:
                return memo[(r,c)]
            ans=float("inf")
            if c>0:
                ans=min(ans,dp(r-1,c-1)+matrix[r][c])
            if c+1<len(matrix[0]):
                ans=min(ans,dp(r-1,c+1)+matrix[r][c])
            memo[(r,c)]=min(ans,dp(r-1,c)+matrix[r][c])
            return memo[(r,c)]
        memo={}
        res=float("inf")
        for c in range(len(matrix[0])):
            res=min(res,dp(len(matrix)-1,c))
        return res
