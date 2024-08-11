from typing import List

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        # Initialize island count
        self.count = 0

        # Define DFS function
        def dfs(i, j):
            # Mark the current cell as visited
            self.visited[(i, j)] = True

            # Explore the neighboring cells
            if j - 1 >= 0 and grid[i][j - 1] == "1" and (i, j - 1) not in self.visited:
                dfs(i, j - 1)
            if j + 1 < len(grid[0]) and grid[i][j + 1] == "1" and (i, j + 1) not in self.visited:
                dfs(i, j + 1)
            if i - 1 >= 0 and grid[i - 1][j] == "1" and (i - 1, j) not in self.visited:
                dfs(i - 1, j)
            if i + 1 < len(grid) and grid[i + 1][j] == "1" and (i + 1, j) not in self.visited:
                dfs(i + 1, j)

        # Initialize visited dictionary
        self.visited = {}

        # Loop through every cell in the grid
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                # If the cell is land and hasn't been visited
                if grid[i][j] == '1' and (i, j) not in self.visited:
                    self.count += 1
                    dfs(i, j)

        # Return the total number of islands
        return self.count
