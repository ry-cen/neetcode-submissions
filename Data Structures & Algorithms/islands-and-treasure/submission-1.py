class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        inf = 2147483647
        n = len(grid)
        m = len(grid[0])

        def dfs(i, j, dist):
            if grid[i][j] == -1 or dist > grid[i][j]:
                return

            if grid[i][j] != 0:
                grid[i][j] = min(dist, grid[i][j])

            directions = ((1, 0), (-1, 0), (0, 1), (0, -1))

            for dr, dc in directions:
                nextr = i + dr
                nextc = j + dc

                if 0 <= nextr < n and 0 <= nextc < m:
                    dfs(nextr, nextc, dist + 1)

        for i in range(n):
            for j in range(m):
                if grid[i][j] == 0:
                    dfs(i, j, 0)

