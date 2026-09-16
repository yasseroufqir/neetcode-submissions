class Solution:
    def isHappy(self, n: int) -> bool:
        def sumSquares(n):
            res = 0
            while n:
                digit = n% 10
                res += digit**2
                n = n // 10
            return res
        visit = set()
        while n not in visit:
            visit.add(n)
            n = sumSquares(n)
            if n == 1:
                return True
            
        return False