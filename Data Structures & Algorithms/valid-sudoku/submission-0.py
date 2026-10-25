class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        cur_square = set()

        for r in range(9):
            cur_row = set()
            cur_col = set()
            for c in range(9):
                row_value = board[r][c]
                col_value = board[c][r]
                square_pos = (r // 3, c // 3)
                if row_value != ".":
                    if row_value in cur_row or (square_pos, row_value) in cur_square:
                        return False
                    cur_row.add(row_value)
                    cur_square.add((square_pos, row_value))

                if col_value != ".":
                    if col_value in cur_col:
                        return False
                    cur_col.add(col_value)
        return True
            