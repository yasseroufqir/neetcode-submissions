class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res , sol = [] , []
        def backtrack(i):
            #at each step i have two choices : take or leave
            if i == len(nums): #reached the end
                res.append(sol[:])
                return
            #leave
            backtrack(i+1)
            #take
            sol.append(nums[i])
            backtrack(i+1)
            sol.pop()
        backtrack(0)
        return res