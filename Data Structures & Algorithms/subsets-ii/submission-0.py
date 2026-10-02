class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        res , sol = [] , []
        nums.sort()
        seen = set()
        def backtrack(i):
            if i == len(nums):
                if tuple(sol[:]) not in seen:
                    res.append(sol[:])
                    seen.add(tuple(sol[:]))
                return
            backtrack(i+1)
            sol.append(nums[i])
            backtrack(i+1)
            sol.pop()
        backtrack(0)
        return res
                