class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        q = deque()
        visited = set()
        rows , cols = len(grid) , len(grid[0])
        #queue is [(day,i,j)] 
        #first step is initialise the queue with rotting oranges
        for i in range(rows):
            for j in range(cols):
                if grid[i][j]==2:
                    q.append((0,i,j))
        max_days = 0
        while q:
            day , row , col = q.popleft()
            max_days = max(day,max_days)
            visited.add((row,col))
            possible = [(1,0),(-1,0),(0,1),(0,-1)]
            for x , y in possible:
                new_row = row + x 
                new_col = col + y
                if 0<=new_row <rows and 0<=new_col < cols and not (new_row,new_col) in visited and grid[new_row][new_col] == 1:
                    grid[new_row][new_col] = 2
                    q.append((day+1,new_row,new_col))
        for i in range(rows):
            for j in range(cols):
                if grid[i][j]==1:
                    return -1
        return max_days
                

