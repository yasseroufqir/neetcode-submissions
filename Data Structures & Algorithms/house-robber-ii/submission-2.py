class Solution:
    def rob(self, nums: List[int]) -> int:
        
        def help(nums):
            rob1 , rob2 = 0, 0
            for n in nums:
                newRob = max(rob1+n,rob2)
                rob1 = rob2
                rob2 = newRob
            return rob2
        return max(help(nums[1:]),help(nums[:-1]),nums[0])