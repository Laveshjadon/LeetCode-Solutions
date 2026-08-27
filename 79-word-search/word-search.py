class Solution(object):
    def exist(self, board, word):
        m = len(board)
        n = len(board[0])

        def backtrack(r,c,k):
            if k == len(word):
                return True
            if r < 0 or r >= m or c >= n or c < 0 or board[r][c] != word[k]:
                return False
            temp = board[r][c]
            board[r][c] = '@'

            res = (backtrack(r + 1, c, k+1)     or backtrack(r -1, c, k+1)       or
            backtrack(r,c+1,k+1) or backtrack(r,c-1,k+1))

            board[r][c] = temp
            return res



        for i in range(m):
            for j in range(n):
                if board[i][j] == word[0]:
                    if backtrack(i,j,0):
                        return True
        return False 



        