from typing import List


def solution(grid: List[list[int]]):
    result = 0
    for i, items in enumerate(grid):
        for j, item in enumerate(items):
            result += dfs(grid, i, j)
    return result


def dfs(grid: List[List[int]], x: int, y: int):
    x_len = len(grid)
    cnt = 1
    if x_len == 0:
        return 0
    y_len = len(grid[0])
    if x < 0 or y < 0 or x >= x_len or y >= y_len or grid[x][y] == 0:
        return 0
    grid[x][y] = 0
    dfs(grid, x+1, y)
    dfs(grid, x, y+1)
    dfs(grid, x-1, y)
    dfs(grid, x, y-1)
    return cnt


if __name__ == '__main__':
    isConnected = [[1, 0, 0, 1],
                   [0, 1, 1, 0],
                   [0, 1, 1, 1],
                   [1, 0, 1, 1]]
    ret = solution(isConnected)
    print(ret)