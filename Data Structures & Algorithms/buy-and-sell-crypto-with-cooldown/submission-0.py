class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        #state is either buy or sell
        # if i buy i increment the i by 1
        #if i sell i increment i by 2
        # dp a cache that has the index and a boolean as 
        dp = {} #(i,buy/sell) as a key and profit as a value
        def dfs(i,buying):
            if (i,buying) in dp:
                return dp[(i,buying)]
            if i >= len(prices):
                return 0
            cooldown = dfs(i+1,buying)
            if buying:
                buy = dfs(i+1, not buying) - prices[i]
                dp[(i,buying)] = max(buy,cooldown)
            else:
                sell = dfs(i+2,not buying) + prices[i]
                dp[(i,buying)] = max(sell,cooldown)
            return dp[(i,buying)]
        return dfs(0,True)