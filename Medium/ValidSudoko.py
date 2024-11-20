'''
Determine if a 9 x 9 Sudoku board is valid. Only the filled cells need to be validated according to the following rules:

Each row must contain the digits 1-9 without repetition.
Each column must contain the digits 1-9 without repetition.
Each of the nine 3 x 3 sub-boxes of the grid must contain the digits 1-9 without repetition.
Note:

A Sudoku board (partially filled) could be valid but is not necessarily solvable.
Only the filled cells need to be validated according to the mentioned rules.
'''
class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows=[set() for i in range(9)]
        cols=[set() for i in range(9)]
        box=[set() for i in range(9)]

        for r in range(9):
            for c in range(9):
                value=board[r][c]
                if value==".":
                    continue
                if value in rows[r]:
                    return False
                else:
                    rows[r].add(value)
                if value in cols[c]:
                    return False
                else:
                    cols[c].add(value)
                ix=(r//3)*3+c//3
                if value in box[ix]:
                    return False
                else:
                    box[ix].add(value)
        return True
