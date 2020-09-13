class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        
        
        def backtracking(board, r, c, rest_word):
            if len(rest_word) == 0: return True
            
            adj_r = [0,0,1,-1]
            adj_c = [1,-1,0,0]
            
            for i in range(4):
                next_r = r + adj_r[i]
                next_c = c + adj_c[i]
                
                if 0 <= next_r < len(board) and 0 <= next_c < len(board[0]) and board[next_r][next_c] == rest_word[0]:
                    tmp = board[next_r][next_c]
                    board[next_r][next_c] = '-'
                    if backtracking(board, next_r, next_c, rest_word[1:]):
                        return True
                    board[next_r][next_c] = tmp
                    
            return False
        
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == word[0]:
                    tmp = board[i][j]
                    board[i][j] = '-'
                    if backtracking(board, i, j, word[1:]):
                        return True
                    board[i][j] = tmp
                
        return False
