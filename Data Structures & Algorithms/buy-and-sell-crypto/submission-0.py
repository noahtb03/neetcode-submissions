class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        current_min = prices[0]
        max_profit = 0
        for num in prices:
            current_min = min(current_min, num)
            profit = num - current_min
            max_profit = max(max_profit, profit)

        return max_profit