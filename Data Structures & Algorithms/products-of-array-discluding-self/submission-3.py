class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = [1]*len(nums)
        n = len(nums)
        prefix =1
        for i in range(len(nums)):
            res[i] = prefix
            prefix*=nums[i]
        #suffixes
        suffix = 1
        for i in range(n-1,-1,-1):
            res[i]*=suffix
            suffix*=nums[i]

        return res
        
