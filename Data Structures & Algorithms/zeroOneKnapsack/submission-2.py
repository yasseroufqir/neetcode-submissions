class Solution:
    def maximumProfit(self, profit: List[int], weight: List[int], capacity: int) -> int:
        memo = {}
        def dfs(i,cap): #profit
            if i == len(profit): 
                return 0
            if (i,cap) in memo:
                return memo[(i,cap)]
            #skip item i
            maxP = dfs(i+1,cap)
            #include item i
            if cap - weight[i]>=0:
                p = profit[i]+dfs(i+1,cap-weight[i])
                maxP = max(maxP,p)
                memo[(i,cap)] = maxP
            return maxP
        return dfs(0,capacity)