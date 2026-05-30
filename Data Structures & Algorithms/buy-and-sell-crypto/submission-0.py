class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        """
        Possible solutions:
        - Double for loop with complexity O(n^2)
        - Iterating through from the back, keeping track of highest possible prices and max profit
        """
        best_sale_price = 1
        max_profit = 0
        for i in range(len(prices) - 1, 0, -1):
            if prices[i] > best_sale_price:
                best_sale_price = prices[i]
            max_profit = max(max_profit, best_sale_price - prices[i - 1])
        max_profit = max(max_profit, 0)
        return max_profit
            