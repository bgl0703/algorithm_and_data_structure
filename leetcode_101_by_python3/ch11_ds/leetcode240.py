from typing import List


class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        len_x, len_y = len(matrix), len(matrix[0])
        i, j = len_x - 1, 0
        flag = True
        while i >= 0:
            if matrix[i][0] > target:
                i -= 1
            else:
                flag = False
                break
        if flag:
            return False

        while j < len_y and i >= 0:
            if matrix[i][j] == target:
                return True
            elif matrix[i][j] < target:
                j += 1
            elif matrix[i][j] > target:
                i -= 1
        return False




if __name__ == '__main__':
    # ma = [[1,4,7,11,15],[2,5,8,12,19],[3,6,9,16,22],[10,13,14,17,24],[18,21,23,26,30]]
    ma = [[-1, 3]]
    s = Solution()
    ret = s.searchMatrix(ma, 3)
    print(ret)