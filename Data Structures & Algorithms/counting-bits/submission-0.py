class Solution:
    def countBits(self, n: int) -> List[int]:
        def countones(n):
            res=0
            while n: 
                if n & 1:
                    res+=1
                n = n >> 1
            return res
        return [countones(i) for i in range(n+1)]