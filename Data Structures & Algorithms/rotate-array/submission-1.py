class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        #i want the last k elements to move to the front
        k %= len(nums)
        nums[:] = nums[-k:] + nums[:-k]