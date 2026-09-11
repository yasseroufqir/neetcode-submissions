class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        seen = set()
        res = False
        for i in nums:
            if i in seen:
                res = True
            seen.add(i)
        return res