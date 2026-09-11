class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        res1, res2 = 0,0
        for i in range(1,len(nums)+1):
            res1+=i
            res2+= nums[i-1]
        return res1 - res2
        
