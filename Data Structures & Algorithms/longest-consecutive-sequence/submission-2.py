class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        setNums, res = set(nums) , 0
        for e in setNums:
            #check if e is the start of a sequence
            if (e-1) not in setNums:
                length = 1
                while e+length in setNums:
                    length+=1
                res = max(res,length)
        return res        