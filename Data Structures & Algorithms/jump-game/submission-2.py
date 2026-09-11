class Solution:
    def canJump(self, nums: List[int]) -> bool:
        max_reach = 0
        for i in range(len(nums)):
            # We can't even reach this position
            if i > max_reach:
                return False
            # Furthest position we can reach from here
            max_reach = max(max_reach, i + nums[i])
            # We can already reach the end
        if max_reach >= len(nums) - 1:
            return True
        return False
                