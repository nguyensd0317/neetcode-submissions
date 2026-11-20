class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        self.matrix = matrix
        rows = len(matrix)
        columns = len(matrix[0])

        for c in range(1, columns):
            matrix[0][c] += matrix[0][c-1]

        for r in range(1, rows):
            matrix[r][0] += matrix[r-1][0]

        for r in range(1, rows):
            for c in range(1,columns):
                matrix[r][c] += matrix[r-1][c]
                matrix[r][c] += matrix[r][c-1]
                matrix[r][c] -= matrix[r-1][c-1]






        

        
    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        a = self.matrix[row2][col2]
        b = self.matrix[row1-1][col2] if row1 > 0 else 0   
        c = self.matrix[row2][col1-1] if col1 > 0 else 0
        d =self.matrix[row1-1][col1-1] if row1 > 0 and col1 > 0 else 0

        return a - b - c + d

        


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)