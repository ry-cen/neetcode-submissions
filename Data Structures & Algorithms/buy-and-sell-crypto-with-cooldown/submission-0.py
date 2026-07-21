class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)

        dp = [[0] * 2 for _ in range(n)]

        for i in range(len(dp) - 1, -1, -1):
            dp[i][1] = max(dp[i+1][1] if i + 1 < n else 0, dp[i+1][0] - prices[i] if i + 1 < n else -prices[i])
            dp[i][0] = max(dp[i+1][0] if i + 1 < n else 0, dp[i+2][1] + prices[i] if i + 2 < n else prices[i])

        return dp[0][1]