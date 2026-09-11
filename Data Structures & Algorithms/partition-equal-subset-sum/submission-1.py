class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        #computes the sum of elements of a subset
        def sumSub(l):
            res = 0
            for i in l:
                res+=i
            return res
        
        if sumSub(nums) % 2 != 0 : return False
        target = sumSub(nums) // 2
        n = len(nums)
        memo={}
        def dfs(i,curr_sum):
            
            if i == n or curr_sum > target:
                return False
            if curr_sum == target: #we only need to find one subset
                return True
            if (i,curr_sum) in memo:
                return memo[(i,curr_sum)]
            take = dfs(i+1,curr_sum + nums[i])
            skip = dfs(i+1,curr_sum)
            memo[(i,curr_sum)] = take or skip
            return memo[(i,curr_sum)]
        return dfs(0,0)