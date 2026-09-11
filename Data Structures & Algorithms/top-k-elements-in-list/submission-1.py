class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        Map = {}
        res = []
        #create a hashmap for each element and its frequency
        for e in nums: 
            if e in Map:
                Map[e]+=1
            else:
                Map[e]=1
        sorted_Map = sorted(Map.items(), key = lambda x:x[1])
        for i in range(k):
            res.append(sorted_Map[len(sorted_Map)-i-1][0])
        return res

