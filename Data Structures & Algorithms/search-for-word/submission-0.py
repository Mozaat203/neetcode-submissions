class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
       rows,columns = len(board), len(board[0])
       path = set()

       def dfs( row, column , index):
            if index == len(word):
                return True
            
            if (min(row,column)<0 or row >= rows or column >= columns or word[index] != board[row][column] or (row,column) in path):
                return False
            path.add((row,column))

            res = (dfs(row + 1, column, index + 1) or
                   dfs(row - 1, column, index + 1) or
                   dfs(row , column + 1, index + 1) or
                   dfs(row , column - 1, index + 1))
            path.remove((row,column))
            return res

       for r in range(rows):
            for c in range(columns):
                if dfs(r,c,0):
                    return True
        
       return False


