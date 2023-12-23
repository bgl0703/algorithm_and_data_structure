from typing import List
# import heapq

class Solution:
    def maxProfit(self, k: int, prices: List[int]) -> int:
        n = len(prices)
        dp = [[[0] * 2 for _ in range(k + 1)] for _ in range(n)]
        for j in range(1, k + 1):
            dp[0][j][1] = -prices[0]
        for i, price in enumerate(prices[1:], 1):
            for j in range(1, k + 1):
                dp[i][j][0] = max(dp[i - 1][j][1] + price, dp[i - 1][j][0])
                dp[i][j][1] = max(dp[i - 1][j - 1][0] - price, dp[i - 1][j][1])
            # print(f"dp===== {dp}")
        return dp[n - 1][k][0]


if __name__ == '__main__':
    prices = [1,2,4,2,5,7,2,4,9,0]
    k = 2
    s = Solution()
    ret = s.maxProfit(k, prices)
    print(ret)