class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        maxRes = nums[0]
        curSum = 0
        for n in nums:
            if curSum < 0:
                curSum = 0
            curSum += n
            maxRes = max(maxRes,curSum)
        return maxRes