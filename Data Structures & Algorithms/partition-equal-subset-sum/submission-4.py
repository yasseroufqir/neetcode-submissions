class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        if sum(nums)% 2:
            return False
        target = sum(nums)/2
        memo = {}
        def dfs(i,curr_sum):
            if curr_sum == target:
                return True
            elif i == len(nums) or curr_sum > target:
                return False
            elif (i,curr_sum) in memo:
                return memo[(i,curr_sum)]
            #i either take nums[i] or not
            take = dfs(i+1,curr_sum+nums[i])
            skip = dfs(i+1,curr_sum)
            memo[(i,curr_sum)] = take or skip
            return memo[(i,curr_sum)]
        return dfs(0,0)