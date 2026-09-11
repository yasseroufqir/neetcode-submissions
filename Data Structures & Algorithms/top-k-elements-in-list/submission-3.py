class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        Map = {}
        res = []
        for e in nums:
            Map[e]= 1 + Map.get(e,0)

        # Bucket: index = frequency
        frequence = [[] for _ in range(len(nums) + 1)]

        for e, cnt in Map.items():
            frequence[cnt].append(e)

        # Go from highest frequency to lowest
        for i in range(len(frequence) - 1, 0, -1):
            for e in frequence[i]:
                res.append(e)

                if len(res) == k:
                    return res