class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        rows,cols = len(grid) , len(grid[0])
        visit = set()
        def dfs(r,c):
            if (r,c) in visit:
                return 0
            if r == rows or c == cols or grid[r][c] == 0 or r<0 or c<0:
                return 0
            visit.add((r,c))
            return 1+dfs(r+1,c)+dfs(r-1,c)+dfs(r,c+1)+dfs(r,c-1)

        res = 0
        
        for r in range(rows):
            for c in range(cols):
                res = max(res,dfs(r,c))
        return res

