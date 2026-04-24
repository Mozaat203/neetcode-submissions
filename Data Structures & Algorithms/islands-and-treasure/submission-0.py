class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        """
        Do not return anything, modify grid in-place instead.
        """
        if not grid:
            return

        rows, cols = len(grid), len(grid[0])
        queue = deque()
        INF = 2147483647
        
        # 1. Architecture Step: Seeding the Frontier
        # Find all treasure chests (0s) to start the multi-source expansion.
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 0:
                    queue.append((r, c))
        
        # 2. Architecture Step: Directional Vectors
        # Standard 4-directional offsets: Right, Left, Down, Up
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        
        # 3. BFS Engine
        while queue:
            r, c = queue.popleft()
            
            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                
                # Boundary Check and INF Gatekeeper
                # We only visit land cells (INF). Water (-1) and 
                # already-filled distances will be ignored.
                if 0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] == INF:
                    # Logic: Neighbor distance = Current distance + 1
                    grid[nr][nc] = grid[r][c] + 1
                    # Append new coordinate to propagate further
                    queue.append((nr, nc))