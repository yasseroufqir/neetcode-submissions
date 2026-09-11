class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        curm,curM = 1 , 1
        res = nums[0]
        for n in nums:
            tmp = curM*n
            curM = max(curM*n,curm*n,n)
            curm = min(n*curm,n,tmp)
            res = max(res,curM)
        return res