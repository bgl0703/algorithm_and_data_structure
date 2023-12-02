from typing import List


class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        grid_x = len(grid)
        grid_y = len(grid[0])
        dp = [[0 for _ in range(grid_y)] for _ in range(grid_x)]
        for j, value in enumerate(grid[0]):
            dp[0][j] = dp[0][max(j-1, 0)] + value
        for i in range(1, grid_x):
            dp[i][0] = dp[i-1][0] + grid[i][0]

        for i in range(1, grid_x):
            for j in range(1, grid_y):
                dp[i][j] = min(dp[i-1][j], dp[i][j-1]) + grid[i][j]
        return dp[grid_x - 1][grid_y - 1]


if __name__ == '__main__':
    grid =[[1, 3, 1], [1, 5, 1], [4, 2, 1]]

    s = Solution()
    res = s.minPathSum(grid)
    print(res)