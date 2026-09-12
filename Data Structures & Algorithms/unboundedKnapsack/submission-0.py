class Solution:
    def maximumProfit(self, profit: List[int], weight: List[int], capacity: int) -> int:
        memo = {}
        def dfs(i,cap):
            if i == len(profit):
                return 0
            if (i,cap) in memo:
                return memo[(i,cap)]
            #skip
            maxP = dfs(i+1,cap)
            #take it 
            if cap - weight[i]>=0:
                maxP = max(maxP,profit[i]+dfs(i,cap-weight[i]))
            memo[(i,cap)] = maxP
            return maxP
        return dfs(0,capacity)