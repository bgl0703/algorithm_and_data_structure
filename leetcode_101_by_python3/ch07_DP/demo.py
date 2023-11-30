from typing import List


def solution(grid: List[List[int]]):
    max_res = 0
    for i, item in enumerate(grid):
        for j, value in enumerate(item):
            max_res = max(dfs(grid, i, j), max_res)

    return max_res


def dfs(grid: List[List[int]], x: int, y: int):
    x_len = len(grid)
    if x_len == 0:
        return 0
    y_len = len(grid[0])
    cnt = 0

    if x < 0 or y < 0 or x >= x_len or y >= y_len or grid[x][y] == 0:
        return 0

    grid[x][y] = 0
    cnt += 1
    cnt += dfs(grid, x+1, y)
    cnt += dfs(grid, x, y+1)
    cnt += dfs(grid, x-1, y)
    cnt += dfs(grid, x, y-1)
    return cnt


if __name__ == '__main__':
    grid = [[0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0],
            [0, 1, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 1, 0, 0, 1, 1, 0, 0, 1, 0, 1, 0, 0],
            [0, 1, 0, 0, 1, 1, 0, 0, 1, 1, 1, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0]]

    ret = solution(grid)

    print(ret)