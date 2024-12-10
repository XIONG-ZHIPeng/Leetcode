class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        length, profit = len(prices), 0
        if length == 1:
            return profit
        #1 = holding a stock, 0 = not holding a stock
        dp = [[0 for _ in range(2)] for i in range(length)]
        dp[0][1] = - prices[0]

        for i in range(1,length):
            dp[i][0] = max(dp[i-1][0], prices[i] + dp[i-1][1])
            dp[i][1] = max(dp[i-1][1], dp[i-2][0] - prices[i], -prices[i])

        return dp[-1][0]



        