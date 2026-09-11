class Solution:
    def findMissingAndRepeatedValues(self, grid: List[List[int]]) -> List[int]:
        n = len(grid)
        #compute S and Q
        S , Q = 0 , 0
        for i in range(1,n**2 + 1):
            S+=i
            Q+= i**2

        #compute sum and sqsum of grid:
        T , R = 0 , 0
        for i in range(n):
            for j in range(n):
                T += grid[i][j]
                R += grid[i][j]**2

        d = T - S
        s = (R-Q)//d

        return [(s+d)//2,(s-d)//2]