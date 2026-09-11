class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}
        for i , n in enumerate(nums):
            seen[n] = i
        for i in range(len(nums)):
            diff = target - nums[i]
            if diff in seen and seen[diff]!= i:
                val1 = seen[diff]
                val2 = i
        return [val1,val2] if val1 < val2 else [val2,val1]