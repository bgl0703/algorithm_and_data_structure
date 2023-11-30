from typing import List


# class Solution:
#     def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
#         cnt = 0
#         for i, line in enumerate(grid):
#             for j, _ in enumerate(line):
#                 cnt = max(self.dfs(grid, i, j), cnt)
#         return cnt
#
#     def dfs(self, grid: List[List[int]], x, y) -> int:
#
#         if x < 0 or y < 0 or x >= len(grid) or y >= len(grid[0]) or grid[x][y] != 1:
#             return 0
#         grid[x][y] = 0
#         cnt = 1
#
#         cnt += self.dfs(grid, x+1, y)
#         cnt += self.dfs(grid, x, y+1)
#         cnt += self.dfs(grid, x-1, y)
#         cnt += self.dfs(grid, x, y-1)
#         return cnt
"""
dfs 先写停止条件
"""


class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        cnt = 0
        for i, line in enumerate(grid):
            for j, _ in enumerate(line):
                res = self.dfs(grid, i, j)
                if res:
                    cnt += 1
        return cnt

    def dfs(self, grid: List[List[str]], x, y) -> bool:
        if x < 0 or y < 0 or x >= len(grid) or y >= len(grid[0]) or grid[x][y] != "1":
            return 0
        grid[x][y] = "0"
        cnt = 1
        cnt += self.dfs(grid, x+1, y)
        cnt += self.dfs(grid, x, y+1)
        cnt += self.dfs(grid, x-1, y)
        cnt += self.dfs(grid, x, y-1)

        if cnt > 0:
            return True
        else:
            return False




if __name__ == '__main__':
    grid = [
        ["1", "1", "0", "0", "0"],
        ["1", "1", "0", "0", "0"],
        ["0", "0", "1", "0", "0"],
        ["0", "0", "0", "1", "1"]
    ]
    s = Solution()
    cnt = s.numIslands(grid)
    print(cnt)

