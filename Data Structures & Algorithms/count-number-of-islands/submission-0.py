class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        n = len(grid)
        m = len(grid[0])
        res = 0
        
        def dfs(i, j):

            grid[i][j] = "-1"

            directions = [(0,1), (0,-1), (1,0), (-1,0)]

            for d in directions:
                di = d[0] + i
                dj = d[1] + j
                if directionIsValid(di, dj) and grid[di][dj] == "1":
                    dfs(di, dj)

        def directionIsValid(di, dj):
            return di >= 0 and dj >= 0 and di < n and dj < m

        for i in range(n):
            for j in range(m):
                if grid[i][j] == "1":
                    dfs(i, j)
                    res += 1

        return res