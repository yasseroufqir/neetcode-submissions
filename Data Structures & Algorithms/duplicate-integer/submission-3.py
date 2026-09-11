class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        seen = []
        for e in nums:
            if e in seen:
                return True
            else:
                seen.append(e)
        return False