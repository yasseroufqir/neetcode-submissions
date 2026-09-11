class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices) <= 1: return 0
        res = 0
        l , r = 0 , 1
        while r < len(prices):
            diff = prices[r] - prices[l]
            if diff <= 0:
                l = r
            else:
                res = max(res,diff)
            r+=1
        return res