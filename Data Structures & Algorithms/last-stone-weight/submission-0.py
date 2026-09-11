import heapq
class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        arr = [-x for x in stones]
        heapq.heapify(arr)
        while len(arr)>=2:
            x = - heapq.heappop(arr)
            y = - heapq.heappop(arr)
            if y < x :
                heapq.heappush(arr,-(x-y))
        return -arr[0] if arr else 0
            