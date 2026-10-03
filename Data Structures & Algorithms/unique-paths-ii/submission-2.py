class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        memo = {}
        m , n = len(obstacleGrid) , len(obstacleGrid[0])
        def dfs(i,j):
            if i == m-1 and j == n-1 and obstacleGrid[i][j] == 0:
                return 1
            if i == m or j == n or obstacleGrid[i][j]:
                return 0
            if (i,j) in memo:
                return memo[(i,j)]
            memo[(i,j)] = dfs(i,j+1)+dfs(i+1,j)
            return memo[(i,j)]
        return dfs(0,0)