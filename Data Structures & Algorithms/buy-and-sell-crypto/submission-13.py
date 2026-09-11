class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        l , r = 0 , 1
        while r<len(prices):
            diff = prices[r]-prices[l]
            if prices[l] > prices[r]:
                l=r
            else:
                profit = max(diff,profit)
            r+=1
        return profit