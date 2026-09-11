class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        #the naive approach is trying every subsequence 2^n which F up
        #the idea is that dp[i] is the LIS starting at index i
        n = len(nums)
        if n == 1:
            return 1
        dp = [1]*n
        for i in range(n-1,-1,-1):
            for j in range(i+1,n):
                if nums[i]< nums[j]:
                    dp[i] = max(dp[i],1+dp[j])
        return max(dp)
        
            