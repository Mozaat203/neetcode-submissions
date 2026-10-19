class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        Rows, Cols = len(matrix), len(matrix[0])

        self.prefixSum2D = [[0] * (Cols + 1) for _ in range(Rows + 1)]

        for row in range(Rows):
            prefix = 0
            for col in range(Cols):
                above = self.prefixSum2D[row][col + 1]
                prefix += matrix[row][col]

                self.prefixSum2D[row + 1][col + 1] = prefix + above


    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        bottomRight = self.prefixSum2D[row2 + 1][col2 + 1]
        topRight = self.prefixSum2D[row1][col2 + 1]
        bottomLeft = self.prefixSum2D[row2 + 1][col1]
        topLeft = self.prefixSum2D[row1][col1]

        return bottomRight - topRight - bottomLeft + topLeft


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)