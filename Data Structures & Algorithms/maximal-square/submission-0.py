class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        m , n = len(matrix) , len(matrix[0])
        dp = [[0]*n for _ in range(m)]
        #dp(i,j) is the max square ending at (i,j)
        for j in range(n):
            if matrix[0][j] == "1":
                dp[0][j] = 1
        for i in range(m):
            if matrix[i][0] == "1":
                dp[i][0] = 1
        for i in range(1,m):
            for j in range(1,n):
                if matrix[i][j] =="1":
                    dp[i][j] = 1 + min(dp[i-1][j]
                                        ,dp[i-1][j-1]
                                        ,dp[i][j-1])
        return max(max(row) for row in dp)**2