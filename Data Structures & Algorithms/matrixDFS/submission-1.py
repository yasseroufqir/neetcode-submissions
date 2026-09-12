class Solution:
    def countPaths(self, grid: List[List[int]]) -> int:
        rows , cols = len(grid) , len(grid[0])
        visit = set()
        def dfs(i,j):
            if i < 0 or j < 0 or i>=rows or j>=cols or grid[i][j] == 1 or (i,j) in visit:
                return 0
            if i == rows-1 and j == cols-1:
                return 1
            visit.add((i,j))
            path = dfs(i-1,j)+dfs(i+1,j)+dfs(i,j+1)+dfs(i,j-1)
            visit.remove((i,j))
            return path
        return dfs(0,0)