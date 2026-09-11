class Solution:
    def tribonacci(self, n: int) -> int:
        if n == 0 : return 0
        if n == 1 or n == 2 : return 1
        prev1,prev2,prev3 = 0, 1 , 1
        for i in range(3,n+1):
            tmp1,tmp2 = prev1, prev2
            prev1 = prev2
            prev2 = prev3
            prev3+= tmp1
            prev3+= tmp2
        return prev3
        