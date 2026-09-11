class Solution:
    def rob(self, nums: List[int]) -> int:
        if not nums:
            return 0
        n = len(nums)
        dp =[0]*n #dp[i] is what i can rob until house i
        if n == 1:
            return nums[0]
        if n == 2:
            return max(nums)
        for i in range(len(nums)):
            dp[i]=max((dp[i-1],dp[i-2]+nums[i]))
        return dp[n-1]
