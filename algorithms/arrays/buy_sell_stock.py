class Solution:
    """Finds the maximum profit to be gained buying and selling stocks in an array of prices"""

    # Analysis: time = O(n), space = O(1)
    def max_profit(self, prices: list[int]) -> int:
        """Returns the maximum profit to be gained from an array of stock prices"""

        buy_price = prices[0]
        max_profit = 0

        for price in prices:
            max_profit = max(max_profit, price - buy_price)
            buy_price = min(buy_price, price)
        return max_profit

if __name__ == "__main__":
    solution = Solution()

    prices1 = [7,1,5,3,6,4]
    assert solution.max_profit(prices1) == 5, "Test case 1 failed"

    prices2 = [7,6,4,3,1]
    assert solution.max_profit(prices2) == 0, "Test case 2 failed"

    prices3 = [1, 2]
    assert solution.max_profit(prices3) == 1, "Test case 3 failed"

    print("All test cases passed!")