class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l = 0
        r = 1
        maxProfit = 0

        if len(prices) < 2:
            return maxProfit

        while r < len(prices):
            curProfit = prices[r] - prices[l]
            maxProfit = max(curProfit, maxProfit)

            if prices[r] > prices[l]:
                r += 1
            else:
                l += 1
                r = l + 1
        
        return maxProfit