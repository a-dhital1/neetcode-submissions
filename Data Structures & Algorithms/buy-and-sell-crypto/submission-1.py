class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        lowest = float('inf')
        max_profit = 0

        for i in prices:
            if i < lowest:
                lowest = i
            else:
                max_profit = max(max_profit, i - lowest)

        return max_profit