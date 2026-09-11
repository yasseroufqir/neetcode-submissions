class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numset = set(nums)
        res = 0
        for e in nums:
            if (e-1) not in numset:
                length = 1
                while (e+length) in numset:
                    length += 1 
                res = max(length,res)
        return res