class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        row_zero = col_zero = False
        m, n = len(matrix), len(matrix[0])
        for num in matrix[0]:
            if not num:
                row_zero = True
                break
        for i in range(m):
            if matrix[i][0] == 0:
                col_zero = True
                break
        for i in range(1,m):
            for j in range(1,n):
                if not matrix[i][j]:
                    matrix[i][0] = 0
                    matrix[0][j] = 0
        for i in range(1,len(matrix)):
            for j in range(1,len(matrix[0])):
                if matrix[i][0] == 0 or matrix[0][j] == 0:
                    matrix[i][j] = 0
        if row_zero:
            for j in range(n):
                matrix[0][j] = 0
        if col_zero:
            for i in range(m):
                matrix[i][0] = 0