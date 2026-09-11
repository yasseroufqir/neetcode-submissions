class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        #an element i is the start of a sequence if (i-1) not in nums
        setNums = set(nums)
        res = 0
        for i in nums:
            if (i-1) not in setNums:
                length = 1
                while i+length in setNums:
                    length+=1
                res = max(res,length)
        return res