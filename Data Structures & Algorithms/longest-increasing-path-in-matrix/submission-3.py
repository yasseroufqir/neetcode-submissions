class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        m , n = len(matrix) , len(matrix[0])
        memo = {}
        def dfs(i,j,PrevVal):
            if i < 0 or i == m or j < 0 or j == n or matrix[i][j]<= PrevVal: 
                return 0 #impossible paths
            if (i,j) in memo:
                return memo[(i,j)]
            PrevVal = matrix[i][j]
            res = 1 + max(dfs(i,j+1,PrevVal),
                        dfs(i+1,j,PrevVal),
                        dfs(i-1,j,PrevVal),
                        dfs(i,j-1,PrevVal),)
            memo[(i,j)] = res
            return res
        ans = 0
        for i in range(m):
            for j in range(n):
                ans = max(ans,dfs(i,j,-1))
        return ans