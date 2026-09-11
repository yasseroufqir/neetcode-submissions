class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        memo = {}
        def dfs(curr):
            if curr in memo:
                return memo[curr]
            if curr > target:
                return 0
            if curr == target:
                return 1 #valid combinaison
            total = 0
            for c in nums:
                total += dfs(curr+c)
            memo[curr] = total
            return total
        return dfs(0)