import heapq
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        arr = []
        res = []
        for p in points:
            dist = (p[0]**2 + p[1]**2)**0.5
            arr.append((dist,p))
        heapq.heapify(arr)
        for i in range(k):
            d , point = heapq.heappop(arr)
            res.append(point)
        return res
