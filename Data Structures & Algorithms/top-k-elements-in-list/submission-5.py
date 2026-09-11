class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        Map = {}
        res = []
        for e in nums:
            Map[e] = Map.get(e,0)+1
        #a character appears at most len(nums) times
        freq = [[] for i in range(len(nums)+1)]
        for i , cnt in Map.items():
            freq[cnt].append(i)
        for i in range(len(freq)-1,-1,-1):
            for e in freq[i]:
                res.append(e)
                if len(res) == k:
                    return res