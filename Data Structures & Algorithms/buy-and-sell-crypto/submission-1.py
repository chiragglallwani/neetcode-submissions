class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit = 0
        left = 0
        for right in range(1, len(prices)):
            profit = prices[right] - prices[left]
            while profit <= 0 and left < right:
                left +=1
            max_profit = max(profit, max_profit)
        return max_profit

