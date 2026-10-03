class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        # must move down m-1 times and right n-1 time
        #in total n-1 parmi m+n-2
        #in how many ways can we arrange these movements
        if m==1 or n== 1:
            return 1
        if m < n:
            m,n = n , m
        res = 1
        j= 1
        for i in range(m,m+n-1):
            res *= i
            res //= j
            j +=1
        return res
