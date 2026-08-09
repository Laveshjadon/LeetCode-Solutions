class Solution(object):
    def isValidSudoku(self, board):
        # Rows 
        for i in range(9):
            seen = set()
            for j in range(9):
                
                if board[i][j] == '.':
                    continue
                if board[i][j] in seen:
                    return False
                seen.add(board[i][j])

        # checking col
        for j in range(9):
            seen = set()
            for i in range(9):
                
                if board[i][j] == '.':
                    continue
                if board[i][j] in seen:
                    return False
                seen.add(board[i][j])


        # cheking box of 3 * 3
        for rows in range(0,9,3):
            for col in range(0,9,3):
                seen = set()
                for i in range(rows, rows+3):
                    for j in range(col, col+3):
                
                        if board[i][j] == '.':
                            continue
                        if board[i][j] in seen:
                            return False
                        seen.add(board[i][j])


        return True

                
        


        
        