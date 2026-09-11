class Solution:
    def integerBreak(self, n: int) -> int:
        memo = {}
        def dfs(num): #max product we can get from int num
            if num == 1: return 1
            if num in memo:
                return memo[num]
            res = 0 if num == n else num #num should be split while others not really
            for i in range(1,num):
                val = dfs(i)*dfs(num-i)
                res = max(res,val)
            memo[num] = res
            return memo[num]
        return dfs(n)