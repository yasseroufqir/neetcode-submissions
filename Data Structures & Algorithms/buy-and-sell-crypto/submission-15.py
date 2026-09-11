class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        l , r = 0 , 0
        while r < len(prices):
            diff = prices[r] - prices[l]
            if diff <= 0:
                l = r
            else:
                profit = max(profit,diff)
            
            r+=1
        return profit
