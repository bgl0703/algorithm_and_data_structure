from typing import List


class Solution:
    def tri_bonacci(self, n: int) -> int:
        if n == 0:
            return 0
        if n <= 2:
            return 1

        def multiply(a: List[List[int]], b: List[List[int]]) -> List[List[int]]:
            c = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
            for i in range(3):
                for j in range(3):
                    c[i][j] = a[i][0] * b[0][j] + a[i][1] * b[1][j] + a[i][2] * b[2][j]
            return c

        def matrix_pow(a: List[List[int]], n: int) -> List[List[int]]:
            ret = [[1, 0, 0], [0, 1, 0], [0, 0, 1]]
            while n > 0:
                if n & 1:
                    ret = multiply(ret, a)
                n >>= 1
                a = multiply(a, a)
            return ret

        q = [[1, 1, 1], [1, 0, 0], [0, 1, 0]]
        res = matrix_pow(q, n)
        return res[0][2]
