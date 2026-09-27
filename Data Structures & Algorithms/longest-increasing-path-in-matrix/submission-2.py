class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        m , n = len(matrix) , len(matrix[0])
        dp = {}
        def dfs(i,j,prevVal): #computes the lip starting from i,j
            if (i<0 or i >=m or j<0 or j >= n or matrix[i][j] <= prevVal):
                return 0
            if (i,j) in dp:
                return dp[(i,j)]
            res = 1
            prevVal = matrix[i][j]
            res = 1+max(dfs(i-1,j,prevVal),
                        dfs(i,j-1,prevVal),
                        dfs(i+1,j,prevVal),
                        dfs(i,j+1,prevVal))
            dp[(i,j)] = res
            return res

        ans = 0
        for i in range(m):
            for j in range(n):
                ans = max(ans,dfs(i,j,-1))
        return ans