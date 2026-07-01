class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = [set() for _ in range(9)]
        cols = [set() for _ in range(9)]
        squares = [set() for _ in range(9)]

        for i in range(len(rows)):
            for j in range(len(cols)):
                val = board[i][j]
                if val == ".":
                    continue
                square_key = (i // 3) * 3 + (j // 3)
                if val in rows[i] or val in cols[j] or val in squares[square_key]:
                    return False

                rows[i].add(val)
                cols[j].add(val)
                squares[square_key].add(val)
                
        return True 