class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        max_profit, i, j = 0, 0, 0

        curr_buy = prices[i]
        while (j < len(prices) - 1):
            j += 1
            if prices[j] < curr_buy:
                curr_buy = prices[j]
            else:
                profit_j = prices[j] - curr_buy
                max_profit = max(max_profit, profit_j)

        return max_profit
