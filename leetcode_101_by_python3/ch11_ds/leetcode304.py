from typing import List


class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        self.pre_matrix = self.pre_sum(matrix)
        # print(self.pre_matrix)

    def pre_sum(self, matrix: List[List[int]]):
        pre_matrix = [[0] * len(matrix[0]) for _ in range(len(matrix))]
        for i, row in enumerate(matrix):
            for j, value in enumerate(row):
                if i == 0:
                    pre_matrix[i][j] = sum(row[:j + 1])
                else:
                    pre_matrix[i][j] = sum(row[:j+1]) + pre_matrix[i-1][j]
        return pre_matrix


    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:

        if row1 == 0 and col1 != 0:
            res = self.pre_matrix[row2][col2] - \
               self.pre_matrix[row2][col1-1]
        elif col1 == 0 and row1 != 0:
            res = self.pre_matrix[row2][col2] - \
                  self.pre_matrix[row1 - 1][col2]
        elif col1 == 0 and row1 == 0:
            res = self.pre_matrix[row2][col2]
        else:
            res = self.pre_matrix[row2][col2] - \
                   self.pre_matrix[row1-1][col2] - \
                   self.pre_matrix[row2][col1-1] + \
                   self.pre_matrix[row1-1][col1-1]

        return res

if __name__ == '__main__':
    s = NumMatrix([[3,0,1,4,2],[5,6,3,2,1],[1,2,0,1,5],[4,1,0,1,7],[1,0,3,0,5]])
    res = s.sumRegion(2,1,4,3)
    print(res)

