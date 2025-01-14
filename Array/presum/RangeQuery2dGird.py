from typing import List

class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        if not matrix or not matrix[0]:
            self.presum = []
            return

        m, n = len(matrix), len(matrix[0])

        # Create a (m+1) x (n+1) prefix sum matrix initialized to 0
        self.presum = [[0] * (n + 1) for _ in range(m + 1)]
        for i in range(m):
            for j in range(n):
                self.presum[i + 1][j + 1] = self.presum[i][j + 1] + self.presum[i + 1][j] + matrix[i][j] - \
                                            self.presum[i][j]

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        row1, row2, col1, col2 = row1 + 1, row2 + 1, col1 + 1, col2 + 1
        return self.presum[row2][col2] - self.presum[row1 - 1][col2] - self.presum[row2][col1 - 1] + \
            self.presum[row1 - 1][col1 - 1]

# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)