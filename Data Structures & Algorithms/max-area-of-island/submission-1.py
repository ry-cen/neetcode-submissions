class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        n = len(grid)
        m = len(grid[0])
        res = 0
        def dfs(i, j, size):
            if grid[i][j] != 1:
                return size - 1
            grid[i][j] = -1

            directions = ((0, 1), (0, -1), (1, 0), (-1, 0))
            vals = []
            for dr, dc in directions:
                nextr = dr + i
                nextc = dc + j

                if 0 <= nextr < n and 0 <= nextc < m:
                    vals.append(dfs(nextr, nextc, 1))

            return size + sum(vals)

        for i in range(n):
            for j in range(m):
                res = max(res, dfs(i, j, 1))

        return res