class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        row = {}
        col = {}
        square = {}
        
        for i, rows in enumerate(board):    
            for j, item in enumerate(rows):
                if board[i][j] == ".":
                    continue

                if board[i][j] in row and row[board[i][j]] == i:
                    return False
                else:
                    row[board[i][j]] = i
                
                if board[i][j] in col and col[board[i][j]] == j:
                    return False
                else:
                    col[board[i][j]] = j

                square_key = (i // 3, j // 3)
                
                if board[i][j] in square and square[board[i][j]] == square_key:
                    return False
                else:
                    square[board[i][j]] = square_key
        return True
                


                
