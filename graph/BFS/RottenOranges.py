class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        queue = deque()
        fresh_count = 0

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 2:
                    queue.append((r, c, 0))  # (row, column, time)
                elif grid[r][c] == 1:
                    fresh_count += 1

        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        time_elapsed = 0

        while queue:
            r, c, time = queue.popleft()
            time_elapsed = max(time_elapsed, time)

            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                # Check if the adjacent cell is a fresh orange
                if 0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] == 1:
                    grid[nr][nc] = 2  # Mark the orange as rotten
                    queue.append((nr, nc, time + 1))
                    fresh_count -= 1

        return time_elapsed if fresh_count == 0 else -1






