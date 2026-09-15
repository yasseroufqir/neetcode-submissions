class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        target = sum(nums)/2
        def dfs(i,curr):
            #some edge cases
            #we either take it an element or not
            #take or skip
            if i == len(nums) or curr >target:
                return False
            if curr == target:
                return True
            else:
                return dfs(i+1,curr+nums[i]) or dfs(i+1,curr)
            
        return dfs(0,0)        