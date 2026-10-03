class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        memo = {}
        def dfs(i,j): #row,col
            if i == len(triangle)-1:
                return triangle[i][j]
            if (i,j) in memo:
                return memo[(i,j)]
            memo[(i,j)] = triangle[i][j] + min(
                                        dfs(i + 1, j),
                                        dfs(i + 1, j + 1)
                                        )
            return memo[(i,j)]
        return dfs(0, 0)