class CommodityTrader:
    """
    A class to calculate the maximum achievable profit
    from agricultural commodity trading with limited transactions.
    """

    @staticmethod
    def max_profit(max_trades, daily_prices):
        """
        Calculates the maximum profit achievable with at most
        max_trades buy-sell transactions.

        Parameters:
        max_trades (int): Maximum allowed transactions
        daily_prices (list): List of daily commodity prices

        Returns:
        int: Maximum profit
        """

        n = len(daily_prices)

        if n == 0 or max_trades == 0:
            return 0

        if max_trades >= n // 2:
            profit = 0
            for i in range(1, n):
                if daily_prices[i] > daily_prices[i - 1]:
                    profit += daily_prices[i] - daily_prices[i - 1]
            return profit

        dp = [[0] * n for _ in range(max_trades + 1)]

        for t in range(1, max_trades + 1):
            max_diff = -daily_prices[0]

            for d in range(1, n):
                dp[t][d] = max(
                    dp[t][d - 1],
                    daily_prices[d] + max_diff
                )
                max_diff = max(
                    max_diff,
                    dp[t - 1][d] - daily_prices[d]
                )

        return dp[max_trades][n - 1]


if __name__ == "__main__":

    # Example 1
    max_trades1 = 2
    prices1 = [2000, 4000, 1000]
    result1 = CommodityTrader.max_profit(max_trades1, prices1)
    print("Example 1")
    print("Input:", prices1)
    print("Maximum Profit:", result1)
    print("Expected Output: 2000")
    print()

    # Example 2 (Multiple profitable trades)
    max_trades2 = 2
    prices2 = [1000, 3000, 2000, 5000, 4000]
    result2 = CommodityTrader.max_profit(max_trades2, prices2)
    print("Example 2")
    print("Input:", prices2)
    print("Maximum Profit:", result2)
    print()

    # Edge Case: No prices
    print("Edge Case – Empty Prices")
    print("Maximum Profit:", CommodityTrader.max_profit(2, []))
    print()

    # Edge Case: All decreasing prices
    print("Edge Case – All Decreasing Prices")
    print("Maximum Profit:", CommodityTrader.max_profit(2, [5000, 4000, 3000]))
    print()

    # Edge Case: Single day
    print("Edge Case – Single Day")
    print("Maximum Profit:", CommodityTrader.max_profit(2, [2500]))