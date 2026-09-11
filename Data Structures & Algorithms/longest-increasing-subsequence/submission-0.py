class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        #dp[i] is gonna be the longest increasing sub until index i
        n = len(nums)
        if n == 1:
            return 1
        LIS = [1]*n #LIS[i] is the LIS starting at i
        for i in range(n-1,-1,-1):
            for j in range(i+1,n): #looking at elements after i
                if nums[i]<nums[j]:
                   LIS[i] = max(LIS[i],1+LIS[j])
        return max(LIS)


            