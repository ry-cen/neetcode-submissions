class Solution:
    def change(self, amount: int, coins: List[int]) -> int:

        coins.sort()

        dp = [[0] * (len(coins) + 1) for _ in range(amount + 1)]
        dp[0] = [1] * (len(coins) + 1)

        for j in range(len(coins)-1, -1, -1):
            for i in range(len(dp)):
                if i >= coins[j]:
                    dp[i][j] = dp[i][j + 1]
                    dp[i][j] += dp[i - coins[j]][j]

        return dp[-1][0]