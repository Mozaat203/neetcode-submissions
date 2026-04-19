class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        if not grid:
            return 0
            
        rows, cols = len(grid), len(grid[0])
        queue = deque()
        fresh_count = 0
        
        # 1. Scanning and Seeding
        # Instead of rotted_fruit.add(), we push coordinates directly to the queue
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 2:
                    queue.append((r, c))
                elif grid[r][c] == 1:
                    fresh_count += 1
        
        # Edge case: No work to do
        if fresh_count == 0:
            return 0
            
        minutes = 0
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        
        # 2. Multi-Source BFS Engine
        while queue and fresh_count > 0:
            minutes += 1
            # Level-order snapshot: process only oranges currently in the queue
            for _ in range(len(queue)):
                r, c = queue.popleft()
                
                for dr, dc in directions:
                    nr, nc = r + dr, c + dc
                    
                    # Boundary check and state check
                    if 0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] == 1:
                        # Mutation: infect the fruit
                        grid[nr][nc] = 2
                        fresh_count -= 1
                        # Push the NEW coordinate for the next minute's frontier
                        queue.append((nr, nc))
        
        # 3. Final Validation
        # If fresh_count isn't 0, some oranges were isolated (islands)
        return minutes if fresh_count == 0 else -1