class Solution:
    def countPaths(self, grid: List[List[int]]) -> int:
        Rows, Cols= len(grid), len(grid[0])

        def unique(grid:List[List[int]], r:int, c:int, visit:set)-> int:
            if (min(r, c) < 0 or
                r == Rows or c == Cols or
                (r, c) in visit or grid[r][c] == 1):
                return 0
            if r==Rows-1 and c==Cols-1:
                return 1

            visit.add((r,c))

            count= 0

            count += unique(grid, r + 1, c, visit)
            count += unique(grid, r - 1, c, visit)
            count += unique(grid, r, c + 1, visit)
            count += unique(grid, r, c - 1, visit)

            visit.remove((r, c))
            return count

        return unique(grid, 0, 0, set())