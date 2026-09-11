class Solution:
    def reverseBits(self, n: int) -> int:
        res = []
        sum = 0
        for i in range(32):
            if n & 1:
                res.append(1)
            else: 
                res.append(0)
            n =n >> 1
        for i in range(32):
            sum+= (2**i) * res[31-i]
        return sum

