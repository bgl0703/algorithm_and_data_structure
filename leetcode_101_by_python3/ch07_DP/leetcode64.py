from typing import List


def min_path_sum(grid: List[List[int]]) -> int:
    grid_x = len(grid)
    grid_y = len(grid[0])
    dp = [[0 for _ in range(grid_y)] for _ in range(grid_x)]
    x, y = 0, 0
    while x < grid_x:
        while y < grid_y:
            if x == y == 0:
                dp[x][y] = grid[0][0]
            elif y == 0 and x > 0:
                dp[x][y] = dp[x - 1][y] + grid[x][y]
            elif x == 0 and y > 0:
                dp[x][y] = dp[x][y - 1] + grid[x][y]
            elif x > 0 and y > 0:
                dp[x][y] = min(dp[x - 1][y], dp[x][y - 1]) + grid[x][y]
            y += 1
        y = 0
        x += 1
    return dp[grid_x - 1][grid_y - 1]


if __name__ == '__main__':
    grid = [[1, 2, 3], [4, 5, 6]]
    ret = min_path_sum(grid)
    print(ret)