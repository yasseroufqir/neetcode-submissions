class Solution:
    def missingNumber(self, arr: List[int]) -> int:
        n = len(arr)
        r = (arr[-1] - arr[0]) / n
        
        if r == 0:
            return arr[0]

        for i in range(1, n):
            if arr[i] - arr[i-1] != r:
                return int(arr[i-1] + r)
