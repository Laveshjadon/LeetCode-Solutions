class Solution(object):
    def isValidSudoku(self, board):
        # checking rows 
        for i in range(9):
            seen = set()
            for j in range(9):

                if board[i][j] == '.':
                    continue
                if board[i][j] in seen:
                    return False
                seen.add(board[i][j])
        
        # checking columns
        for j in range(9):
            seen = set()
            for i in range(9):

                if board[i][j] == '.':
                    continue
                if board[i][j] in seen:
                    return False
                seen.add(board[i][j])
        # now blocks
        for rows in range(0,9,3):
            for columns in range(0,9,3):

                seen = set()
                for i in range(rows, rows+3):
                    for j in range(columns, columns+3):
                        if board[i][j] == '.':
                            continue
                        if board[i][j] in seen:
                            return False
                        seen.add(board[i][j])

        return True



        
        