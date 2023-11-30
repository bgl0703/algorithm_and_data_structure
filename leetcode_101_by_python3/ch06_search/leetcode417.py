from typing import List


class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        pass

    def dfs_p(self, heights: List[List[int]], x, y, point: int) -> List[int]:
        if x <= 0 or y <= 0:
            return 1

        if x >= len(heights) - 1 or y >= len(heights[0]) - 1:
            return 2

        if heights[x][y] < point:
            return 0

        self.dfs_p(heights, x)

        # if heights[x][y] < heights[x-1][y] and \
        #     heights[x][y] < heights[x][y-1] and \
        #     heights[x][y] < heights[x+1][y] and \
        #     heights[x][y] < heights[x][y+1]:
        #     return 0


if __name__ == '__main__':
    pass