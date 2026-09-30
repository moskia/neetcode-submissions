class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l, r = 0, len(prices)-1
        sell = prices[0]
        maxProfit = 0
        for i in range(1, len(prices)):
            if sell > prices[i]:
                sell = prices[i]
            else: 
                maxProfit = max(maxProfit, prices[i]-sell)

        return maxProfit