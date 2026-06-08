class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        """
        Approach: two pointer/sliding window variable approach, buy the stock on ith day, 
        check when you sell at jth day (j should be minimum i + 1) profit should be > 0 and i < j
        if not then do i++
        """
        left = 0
        max_profit = 0
        for j in range(1, len(prices)):
            profit = prices[j] - prices[left]
            while profit < 0 and left < j:
                left += 1
            max_profit = max(max_profit, profit)
        return max_profit

