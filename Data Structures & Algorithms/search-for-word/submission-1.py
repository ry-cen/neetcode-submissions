class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        n = len(board)
        m = len(board[0])
        
        res = False
        def dfs(idx, i, j, path):
            nonlocal res
            if idx >= len(word)-1:
                res = True
                return

            directions = ((0,1), (1,0), (0,-1), (-1,0))

            possible_directions = [d for d in directions if d[0] + i >= 0 and d[0] + i < n and d[1] + j >= 0 and d[1] + j < m and board[d[0] + i][d[1] + j] == word[idx + 1] and (d[0] + i, d[1] + j) not in path]
            for d in possible_directions:
                dfs(idx + 1, d[0] + i, d[1] + j, path + [(i,j)])

        for i in range(n):
            for j in range(m):
                if board[i][j] == word[0] and not res:
                    dfs(0, i, j, [])
        
        return res