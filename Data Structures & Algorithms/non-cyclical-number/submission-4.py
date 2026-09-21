class Solution:
    def isHappy(self, n: int) -> bool:
        def sumsquares(x):
            s = 0
            while x:
                digit = x%10
                s+= digit**2
                x = x//10
            return s
        seen = set()
        while n not in seen:
            seen.add(n)
            n = sumsquares(n)
        
        return n == 1 