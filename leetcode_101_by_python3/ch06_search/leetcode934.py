from collections import deque
from typing import List
from more_itertools import pairwise


class Solution:
    def shortestBridge(self, grid: List[List[int]]) -> int:



        i, j = next((i, j) for i in range(n) for j in range(n) if grid[i][j])
        self.dfs(i, j)
        ans = 0
        while 1:
            for _ in range(len(q)):
                i, j = q.popleft()
                for a, b in pairwise((-1, 0, 1, 0, -1)):
                    x, y = i + a, j + b
                    if 0 <= x < n and 0 <= y < n:
                        if grid[x][y] == 1:
                            return ans
                        if grid[x][y] == 0:
                            grid[x][y] = 2
                            q.append((x, y))
            ans += 1

    def dfs(self, i, j):
        n = len(grid)
        q.append((i, j))
        grid[i][j] = 2
        for a, b in pairwise((-1, 0, 1, 0, -1)):
            x, y = i + a, j + b
            if 0 <= x < n and 0 <= y < n and grid[x][y] == 1:
                dfs(x, y)


if __name__ == '__main__':
    grid = [[0, 1, 0], [0, 0, 0], [0, 0, 1]]
    s = Solution()
    r = s.shortestBridge(grid)
    print(f"r == {r}")