class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        Map = {}
        
        for n in nums:
            if n in Map:
                Map[n] += 1
            else:
                Map[n] = 1
        
        for key in Map:
            if Map[key] == 1:
                return key
            