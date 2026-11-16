class Solution:
    def BFS(self, grid, visited, i, j):
        if i >= 0 and i < len(grid) and j >= 0 and j < len(grid[0]) and grid[i][j] == '1' and not visited[i][j]:
            visited[i][j] = True
        else:
            return
        
        self.BFS(grid, visited, i + 1, j)
        self.BFS(grid, visited, i - 1, j)
        self.BFS(grid, visited, i, j + 1)
        self.BFS(grid, visited, i, j - 1)

    def numIslands(self, grid: List[List[str]]) -> int:
        m = len(grid)
        n = len(grid[0])

        visited = [[False for _ in range(n)] for _ in range(m)]
        numIslands = 0

        for i in range(m):
            for j in range(n):
                if grid[i][j] == "1" and not visited[i][j]:
                    numIslands += 1
                    self.BFS(grid, visited, i, j)
        
        return numIslands
