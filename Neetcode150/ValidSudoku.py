'''
You are given a a 9 x 9 Sudoku board board. A Sudoku board is valid if the following rules are followed:

Each row must contain the digits 1-9 without duplicates.
Each column must contain the digits 1-9 without duplicates.
Each of the nine 3 x 3 sub-boxes of the grid must contain the digits 1-9 without duplicates.
Return true if the Sudoku board is valid, otherwise return false

Note: A board does not need to be full or be solvable to be valid.
'''
class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        for i in range(9):
            row={}
            for j in range(9):
                if board[i][j] !="." and board[i][j] in row:
                    print("here")
                    return False
                else:
                    row[board[i][j]]=1
        for j in range(9):
            col={}
            for i in range(9):
                if board[i][j] !="." and board[i][j] in col:
                    print("here2")
                    return False
                else:
                    col[board[i][j]]=1
        offsets=[(0,0),(0,3),(0,6),(3,0),(3,3),(3,6),(6,0),(6,3),(6,6)]
        for oi,oj in offsets:
            sub={}
            for i in range(3):
                for j in range(3):
                    if board[i+oi][j+oj] !="." and board[i+oi][j+oj] in sub:
                        return False
                    else:
                        sub[board[i+oi][j+oj]]=1
            print(sub)
        return True
