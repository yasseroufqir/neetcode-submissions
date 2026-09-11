class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        Map = {}
        
        for n in nums:
            Map[n] = Map.get(n,0)+1
        
        for key in Map:
            if Map[key] == 1:
                return key
            